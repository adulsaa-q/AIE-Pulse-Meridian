import sqlite3
from datetime import datetime, timedelta
import config

# ข้อมูลจำลอง — สมมติสถานการณ์ความตึงเครียดในตลาดพลังงาน
MOCK_DATA = {
    "PTT": {
        "search_volume": [20, 22, 19, 21, 23, 20, 65],  # พุ่งกระโดด (ACCELERATION)
        "news_mentions": [1, 0, 2, 1, 1, 0, 5],         # พุ่งกระโดด (ACCELERATION)
    },
    "บางจาก": {
        "search_volume": [30, 28, 31, 29, 30, 28, 12],  # ร่วงหนัก (DECLINE)
        "news_mentions": [0, 1, 0, 0, 1, 0, 0],
    },
    "SPRC": {
        "search_volume": [10, 11, 10, 12, 11, 10, 45],  # พุ่งกระโดด (ACCELERATION)
        "news_mentions": [0, 0, 1, 0, 0, 1, 3],
    },
    "ไทยออยล์": {
        "search_volume": [8, 9, 8, 8, 9, 8, 8],         # คงที่ปกติ (ไม่มี Signal)
        "news_mentions": [0, 0, 0, 1, 0, 0, 1],
    },
    "BAFS": {
        "search_volume": [15, 14, 15, 16, 14, 15, 5],   # ร่วงหนัก (DECLINE)
        "news_mentions": [1, 0, 0, 0, 1, 0, 0],
    },
    # เปลี่ยนชื่อให้ตรงกับ config.KEYWORDS
    "ราคาน้ำมันดิบ": {
        "search_trend_score": [40, 38, 42, 41, 39, 40, 95], # ตลาดกังวลหนัก (ACCELERATION)
        "market_signals": [2, 1, 2, 3, 2, 1, 8],            # ข่าวออกเยอะมาก
    },
}

def seed():
    """ใส่ข้อมูลจำลองย้อนหลัง 7 วันเข้า SQLite"""
    print(f"⏳ กำลังล้างข้อมูลเก่าและสร้างข้อมูลจำลองใหม่ใน {config.DB_PATH}...")
    
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

    # ลบข้อมูลเก่าออกก่อน เพื่อไม่ให้ AI สับสนกับของเก่า
    cursor.execute("DELETE FROM signals")

    # วนลูปสร้างข้อมูลย้อนหลัง 7 วัน
    today = datetime.now()
    count = 0

    for entity, metrics in MOCK_DATA.items():
        for metric_name, values in metrics.items():
            for i, value in enumerate(values):
                # ไล่วันที่จาก 6 วันที่แล้ว จนถึงวันนี้
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
    print(f"✅ Seed สำเร็จ — เพิ่มข้อมูลทั้งหมด {count} records พร้อมทดสอบแล้วครับ")

if __name__ == "__main__":
    seed()