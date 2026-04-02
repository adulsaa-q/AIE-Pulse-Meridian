from pytrends.request import TrendReq
from datetime import datetime 
import config

def collect() -> list[dict]:
    pytrends = TrendReq(hl="th-TH", tz=420)
    records = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ดึงเทรนด์จาก KEYWORDS แทน BRANDS
    for keyword in config.KEYWORDS: 
        try: 
            pytrends.build_payload([keyword], timeframe="now 7-d", geo="TH")
            df = pytrends.interest_over_time()
            if df.empty:
                continue
            latest_value = float(df[keyword].iloc[-1])
            records.append({
                "date": now,
                "entity": keyword,
                "metric_name": "search_trend_score", # ระบุว่าเป็นเทรนด์ตลาด
                "metric_value": latest_value,
                "dimension": "Thailand",
                "source": "google_trends"
            })
        except Exception as e:
            print(f"\n [ERROR] google_trends: {keyword} --> {e}")
    return records