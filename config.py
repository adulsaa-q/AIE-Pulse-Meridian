# config.py
import os

BRANDS = [
    "PTT",
    "SPRC",
    "BAFS",
]

KEYWORDS = [
    "ราคาน้ำมัน",
    "น้ำมันดิบ",
]

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/thai/rss.xml",
    "https://www.blognone.com/node/feed",
]

STRATEGY_MODE    = "growth_focused"
SIGNAL_THRESHOLD_PCT = 20.0
BASELINE_DAYS    = 7
REPORT_OUTPUT_DIR = "reports/"
REPORT_LANGUAGE  = "Thai"
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL     = "gemini-2.5-flash"
SCHEDULE_HOUR    = 8
SCHEDULE_MINUTE  = 0
DB_PATH          = "data/signals.db"