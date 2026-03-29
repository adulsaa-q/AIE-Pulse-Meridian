import sqlite3
import pandas as pd
import config

def detect_signals() -> list[dict]:
    """
    Detect signals from other plugins using a 7-day baseline in SQLite.
    """
    conn = sqlite3.connect(config.DB_PATH)
    df = pd.read_sql(
    "SELECT * FROM signals",
    conn
    )
    conn.close()
    signals = []
    for entity in df["entity"].unique():
        for metric in df["metric_name"].unique():
            subset = df[
                (df["entity"] == entity) &
                (df["metric_name"] == metric)
            ]
            if len(subset) < 2:
                continue
            # AVG of last 7 days excluding today
            baseline = subset["metric_value"].iloc[:-1].mean()
            #current value
            current = subset["metric_value"].iloc[-1]
            #prevent division by zero
            if baseline == 0:
                continue
            # calculate percentage change
            pct_change = (current - baseline) / baseline * 100
            if abs(pct_change) < config.SIGNAL_THRESHOLD_PCT:
                continue
            # Determine the type of signal
            if pct_change >= config.SIGNAL_THRESHOLD_PCT:
                signal_type = "ACCELERATION"
            elif pct_change <= -config.SIGNAL_THRESHOLD_PCT:
                signal_type = "DECLINE"
            else:
                signal_type = "ANOMALY"
                # Append signal to list
            signals.append({
                "entity": entity,
                "metric_name": metric,
                "signal_type": signal_type,
                "current_value": current,
                "baseline": baseline,
                "pct_change": round(pct_change, 2)
            })
    return signals
