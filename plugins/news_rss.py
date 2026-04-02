import feedparser
from datetime import datetime
import config

def collect() -> list[dict]:
    """ดึงข่าวจาก RSS feeds แล้วนับจำนวน mention ของ BRANDS และ KEYWORDS ต่อวัน"""
    today = datetime.now().strftime("%Y-%m-%d")
    counts = {}  # (entity, metric_name) -> จำนวน mention รวมทุก feed

    for feed_url in config.RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                title = entry.get("title", "").lower()

                # 1. เช็คชื่อแบรนด์ (Company Level)
                for brand in config.BRANDS:
                    if brand.lower() in title:
                        key = (brand, "news_mentions")  # ระบุว่าเป็นข่าวของแบรนด์
                        counts[key] = counts.get(key, 0) + 1

                # 2. เช็คปัจจัยตลาด (Market Level)
                for keyword in config.KEYWORDS:
                    if keyword.lower() in title:
                        key = (keyword, "market_signals")  # ระบุว่าเป็นสัญญาณตลาด
                        counts[key] = counts.get(key, 0) + 1

        except Exception as e:
            print(f"[ERROR] news_rss: {feed_url} --> {e}")

    # รวม count ต่อ entity+metric เป็น 1 record ต่อวัน (ป้องกันข้อมูลซ้ำเมื่อรันหลายรอบ)
    records = []
    for (entity, metric_name), count in counts.items():
        records.append({
            "date": today,
            "entity": entity,
            "metric_name": metric_name,
            "metric_value": float(count),
            "dimension": "RSS",
            "source": "news_rss"
        })

    return records
