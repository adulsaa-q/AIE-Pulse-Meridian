from pytrends.request import TrendReq
from datetime import datetime 
import config

def collect() -> list[dict]:
    """
    ดึง search volume ของทุก brand จาก Google Trends
    และ return เป็น list ตาม Universal Schema
    """
    pytrends = TrendReq(hl="th-TH", tz=420)
    records = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Loop through each brand specified in config.py
    for brand in config.BRANDS:
        try: 
            # Configure Google Trends query parameters (keyword, last 7 days, Thailand)
            pytrends.build_payload([brand], timeframe="now 7-d", geo="TH")
            # Retrieve search volume data and store it in a DataFrame
            df = pytrends.interest_over_time()
            if df.empty:
                continue
            latest_value = float(df[brand].iloc[-1]) # get last value
            records.append({
                "date":         now,
                "entity":       brand,
                "metric_name":  "search_volume",
                "metric_value": latest_value,
                "dimension":    "Thailand",
                "source":       "google_trends"
            })
        except Exception as e:
            print(f"\n [ERROR] google_trends: {brand} --> {e}")
    return records