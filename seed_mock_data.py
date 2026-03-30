# seed_mock_data.py
# สร้างข้อมูลจำลองย้อนหลัง 7 วัน สำหรับทดสอบระบบ

import sqlite3
from datetime import datetime, timedelta
import config

# ข้อมูลจำลอง — สมมติสถานการณ์น้ำมันตึงเครียด
MOCK_DATA = {
    "PTT": {
        "search_volume": [20, 22, 19, 21, 23, 20, 65],  # พุ่งขึ้นวันสุดท้าย
        "news_mentions": [1, 0, 2, 1, 1, 0, 5],
    },
    "บางจาก": {
        "search_volume": [30, 28, 31, 29, 30, 28, 12],  # ลดลงวันสุดท้าย
        "news_mentions": [0, 1, 0, 0, 1, 0, 0],
    },
    "SPRC": {
        "search_volume": [10, 11, 10, 12, 11, 10, 45],  # พุ่งขึ้น
        "news_mentions": [0, 0, 1, 0, 0, 1, 3],
    },
    "ไทยออยล์": {
        "search_volume": [8, 9, 8, 8, 9, 8, 8],   # คงที่ปกติ
        "news_mentions": [0, 0, 0, 1, 0, 0, 1],
    },
    "BAFS": {
        "search_volume": [15, 14, 15, 16, 14, 15, 5],  # ลดลง
        "news_mentions": [1, 0, 0, 0, 1, 0, 0],
    },
    "ราคาน้ำมัน": {
        "search_volume": [40, 38, 42, 41, 39, 40, 85],  # พุ่งสูงมาก
        "news_mentions": [2, 1, 2, 3, 2, 1, 8],
    },
}

def seed():
    """ใส่ข้อมูลจำลองย้อนหลัง 7 วันเข้า SQLite"""

    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()

    # สร้างตารางถ้ายังไม่มี
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            date         TEXT,
            entity       TEXT,
            metric_name  TEXT,
            metric_value REAL,
            dimension    TEXT,
            source       TEXT
        )
    """)

    # ลบข้อมูลเก่าออกก่อน
    cursor.execute("DELETE FROM signals")

    # วนลูปสร้างข้อมูลย้อนหลัง 7 วัน
    today = datetime.now()
    count = 0

    for entity, metrics in MOCK_DATA.items():
        for metric_name, values in metrics.items():
            for i, value in enumerate(values):
                date = today - timedelta(days=6-i)
                date_str = date.strftime("%Y-%m-%d %H:%M:%S")

                cursor.execute("""
                    INSERT INTO signals
                    (date, entity, metric_name, metric_value, dimension, source)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    date_str,
                    entity,
                    metric_name,
                    float(value),
                    "Thailand",
                    "mock_data"
                ))
                count += 1

    conn.commit()
    conn.close()
    print(f"✅ Seed สำเร็จ — {count} records เข้า {config.DB_PATH}")

if __name__ == "__main__":
    seed()