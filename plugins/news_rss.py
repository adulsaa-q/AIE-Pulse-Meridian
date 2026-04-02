import feedparser
from datetime import datetime
import config

def collect() -> list[dict]:
    records = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for feed_url in config.RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                title = entry.get("title", "").lower()
                
                # 1. เช็คชื่อแบรนด์ (Company Level)
                for brand in config.BRANDS:
                    if brand.lower() in title:
                        records.append({
                            "date": now,
                            "entity": brand,
                            "metric_name": "news_mentions", # ระบุว่าเป็นข่าวของแบรนด์
                            "metric_value": 1.0,
                            "dimension": feed_url,
                            "source": "news_rss"
                        })
                
                # 2. เช็คปัจจัยตลาด (Market Level)
                for keyword in config.KEYWORDS:
                    if keyword.lower() in title:
                        records.append({
                            "date": now,
                            "entity": keyword, # บันทึกเป็นคำสำคัญ
                            "metric_name": "market_signals", # ระบุว่าเป็นสัญญาณตลาด
                            "metric_value": 1.0,
                            "dimension": feed_url,
                            "source": "news_rss"
                        })
        except Exception as e:
            print(f"\n [ERROR] news_rss: {feed_url} --> {e}")
    return records