import feedparser
from datetime import datetime
import config

def collect() -> list[dict]:
    """
    ดึงข่าวจาก RSS Feed และนับจำนวนครั้งที่ brand ถูกพูดถึง
    return เป็น list ตาม Universal Schema
    """
    records = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for feed_url in config.RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                for brand in config.BRANDS:
                    title = entry.get("title", "").lower()
                    if brand.lower() in title:
                        records.append({
                            "date":         now,
                            "entity":       brand,
                            "metric_name":  "news_mentions",
                            "metric_value": 1.0, # count as 1 mention
                            "dimension":    feed_url, # source feed URL as dimension
                            "source":       "news_rss"
                        })
        except Exception as e:
            print(f"\n [ERROR] news_rss: {feed_url} --> {e}")
    return records