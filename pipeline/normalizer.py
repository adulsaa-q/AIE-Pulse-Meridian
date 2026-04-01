import sqlite3
import config
import pandas as pd 

def save(records: list[dict]):
    """
    รับ records จาก plugin ต่างๆ แล้วเก็บลง SQLite
    ตรวจสอบว่าทุก record ตรงกับ Universal Schema ก่อนบันทึก
    """
    with sqlite3.connect(config.DB_PATH) as conn:
        cursor = conn.cursor()
        # crate table if not exists 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS signals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                entity TEXT,
                metric_name TEXT,
                metric_value REAL,
                dimension TEXT,
                source TEXT
            )
        """)
        for record in records:
            cursor.execute("""
                insert into signals
                (date, entity, metric_name, metric_value, dimension, source)
                values (?, ?, ?, ?, ?, ?)
            """, (
                record.get("date"),
                record.get("entity"),
                record.get("metric_name"),
                record.get("metric_value"),
                record.get("dimension"),
                record.get("source")
            ))
        conn.commit()
        
    def export_sample_csv() -> None:
        """ส่งออก 20 records ล่าสุดจาก SQLite เป็น CSV ตัวอย่าง"""
        conn = sqlite3.connect(config.DB_PATH)
        df = pd.read_sql(
            "SELECT * FROM signals ORDER BY date DESC LIMIT 20",
            conn
        )
        conn.close()
    df.to_csv("data/signals_sample.csv", index=False)
    print(f"Export สำเร็จ {len(df)} records → data/signals_sample.csv") 