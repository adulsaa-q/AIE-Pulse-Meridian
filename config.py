import os
from dotenv import load_dotenv

load_dotenv()
# ============================================================
# USE CASE — เปลี่ยนตรงนี้เพื่อแยก database อัตโนมัติ
# ============================================================
USE_CASE = "energy_sector"

# ============================================================
# BRANDS — โฟกัสเฉพาะชื่อแบรนด์ คู่แข่ง หรือบริษัทที่ต้องการวัดผล
# ============================================================
BRANDS = [
    "PTT",
    "บางจาก",
    "SPRC",
    "ไทยออยล์",
    "BAFS"
]

# ============================================================
# KEYWORDS — ปัจจัยขับเคลื่อนตลาดและบริบทแวดล้อม (Market Drivers)
# ============================================================
KEYWORDS = [
    # หมวดราคาและต้นทุน
    "ราคาน้ำมันดิบ",
    "ค่าการกลั่น",
    "ก๊าซธรรมชาติ",
    # หมวดนโยบายรัฐ
    "กองทุนน้ำมัน",
    "ตรึงราคาน้ำมัน",
    # หมวดภูมิรัฐศาสตร์และอุปทานโลก
    "สงครามตะวันออกกลาง",
    "โอเปก",
    "OPEC",
    # หมวดสินค้าทดแทนและแนวโน้มอนาคต
    "รถ EV",
    "พลังงานสะอาด"
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

# API KEYS & CONFIG
OPENROUTER_API_KEY   = os.getenv("OPENROUTER_API_KEY", "")

# Models AI
#OPENROUTER_MODEL     = "stepfun/step-3.5-flash:free"
#OPENROUTER_MODEL     = "google/gemini-2.0-flash-exp:free"
OPENROUTER_MODEL     = "openrouter/free"

# DB แยกตาม use case อัตโนมัติ
DB_PATH = f"data/{USE_CASE}.db"