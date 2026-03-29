"""
storage.py
Data persistence layer for signal records.
"""

from __future__ import annotations

import sqlite3
from contextlib import closing
from datetime import datetime
from pathlib import Path
from typing import Iterable, Dict, Any

import pandas as pd
import config


DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    entity TEXT NOT NULL,
    metric_name TEXT NOT NULL,
    metric_value REAL,
    dimension TEXT,
    source TEXT
);
"""


REQUIRED_FIELDS = {
    "date",
    "entity",
    "metric_name",
    "metric_value",
    "dimension",
    "source",
}


# -----------------------------
# Database Utilities
# -----------------------------

def get_connection() -> sqlite3.Connection:
    """Create database connection."""
    return sqlite3.connect(config.DB_PATH)


def initialize_db() -> None:
    """Ensure required tables exist."""
    with closing(get_connection()) as conn:
        conn.execute(DB_SCHEMA)
        conn.commit()


# -----------------------------
# Validation
# -----------------------------

def validate_record(record: Dict[str, Any]) -> None:
    """Validate record schema."""
    missing = REQUIRED_FIELDS - record.keys()

    if missing:
        raise ValueError(f"Missing fields: {missing}")


# -----------------------------
# Write Operations
# -----------------------------

def save(records: Iterable[Dict[str, Any]]) -> int:
    """
    Persist records into SQLite.

    Returns:
        int: number of inserted rows
    """
    initialize_db()

    insert_sql = """
        INSERT INTO signals
        (date, entity, metric_name, metric_value, dimension, source)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    rows = []

    for record in records:
        validate_record(record)

        rows.append((
            record["date"],
            record["entity"],
            record["metric_name"],
            record["metric_value"],
            record["dimension"],
            record["source"],
        ))

    with closing(get_connection()) as conn:
        conn.executemany(insert_sql, rows)
        conn.commit()

    return len(rows)


# -----------------------------
# Export
# -----------------------------

def export_sample_csv(limit: int = 20) -> Path:
    """
    Export latest records to CSV.

    Args:
        limit: number of rows to export
    """
    query = """
        SELECT *
        FROM signals
        ORDER BY date DESC
        LIMIT ?
    """

    with closing(get_connection()) as conn:
        df = pd.read_sql(query, conn, params=(limit,))

    output_path = Path("data/signals_sample.csv")
    output_path.parent.mkdir(exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"[EXPORT] {len(df)} rows → {output_path}")

    return output_path