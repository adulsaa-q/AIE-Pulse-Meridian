from pytrends.request import TrendReq
from datetime import datetime
import config

def collect() -> list[dict]:
    """ดึงข้อมูล Google Trends รายสัปดาห์สำหรับ KEYWORDS ทั้งหมด แล้วคืนค่าเป็น records"""
    pytrends = TrendReq(hl="th-TH", tz=420)
    records = []
    today = datetime.now().strftime("%Y-%m-%d")

    # ดึงเทรนด์ตลาดจาก KEYWORDS (ปัจจัยขับเคลื่อนตลาด) ไม่ใช่ BRANDS
    keywords = config.KEYWORDS
    # จัดกลุ่ม batch ละ 5 คำ ตามข้อจำกัดของ pytrends ต่อ 1 request
    batches = [keywords[i:i+5] for i in range(0, len(keywords), 5)]

    for batch in batches:
        try:
            pytrends.build_payload(batch, timeframe="now 7-d", geo="TH")
            df = pytrends.interest_over_time()
            if df.empty:
                continue
            for keyword in batch:
                if keyword not in df.columns:
                    continue
                latest_value = float(df[keyword].iloc[-1])
                records.append({
                    "date": today,
                    "entity": keyword,
                    "metric_name": "search_trend_score",  # ระบุว่าเป็นเทรนด์ตลาด
                    "metric_value": latest_value,
                    "dimension": "Thailand",
                    "source": "google_trends"
                })
        except Exception as e:
            print(f"[ERROR] google_trends batch {batch} --> {e}")

    return records
