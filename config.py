import os
from dotenv import load_dotenv

load_dotenv()
# ============================================================
# USE CASE — เปลี่ยนตรงนี้เพื่อแยก database อัตโนมัติ
# ============================================================
USE_CASE = "energy_sector"

# ============================================================
# BRANDS — ผสมชื่อหุ้น + แบรนด์ + keyword
# ============================================================
BRANDS = [
    "PTT",
    "บางจาก",
    "SPRC",
    "ไทยออยล์",
    "BAFS",
    "ราคาน้ำมัน",
]

KEYWORDS = [
    "น้ำมันดิบ",
    "ราคาน้ำมัน",
    "สงครามตะวันออกกลาง",
]

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/thai/rss.xml",
    "https://www.thairath.co.th/rss/news.xml",
    "https://www.blognone.com/node/feed",
]

STRATEGY_MODE        = "growth_focused"
SIGNAL_THRESHOLD_PCT = 20.0
BASELINE_DAYS        = 7
REPORT_OUTPUT_DIR    = "reports/"
REPORT_LANGUAGE      = "Thai"
GEMINI_API_KEY       = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL         = "gemini-2.5-flash"
#-------------------------------------------
# API KEYS & CONFIG
OPENROUTER_API_KEY   = os.getenv("OPENROUTER_API_KEY", "")
#-------------------------------------------
# Models AI
#OPENROUTER_MODEL     = "stepfun/step-3.5-flash:free"
#OPENROUTER_MODEL     = "google/gemini-2.0-flash-exp:free"
OPENROUTER_MODEL     = "openrouter/free"
#-------------------------------------------
SCHEDULE_HOUR        = 8
SCHEDULE_MINUTE      = 0

# DB แยกตาม use case อัตโนมัติ
DB_PATH = f"data/{USE_CASE}.db"