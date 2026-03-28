# config.py
# AIE — Adaptive Intelligence Engine
# แก้ไขไฟล์นี้เพื่อปรับ system ให้เหมาะกับ use case ของคุณ
# ไม่ต้องแตะไฟล์อื่น

# ============================================================
# 1. BRANDS / ENTITIES ที่ต้องการ track
# ============================================================
BRANDS = [
    "Shopee",
    "Lazada",
    "TikTok Shop",
]

# ============================================================
# 2. KEYWORDS เพิ่มเติมสำหรับ Google Trends
#    (นอกเหนือจาก brand name)
# ============================================================
KEYWORDS = [
    "ซื้อของออนไลน์",
    "โปรโมชั่น",
]

# ============================================================
# 3. RSS FEEDS ที่ต้องการดึงข่าว (ฟรี ไม่ต้อง API key)
# ============================================================
RSS_FEEDS = [
    "https://feeds.bbci.co.uk/thai/rss.xml",           # BBC Thai
    "https://www.thairath.co.th/rss/news.xml",          # ไทยรัฐ
    "https://www.blognone.com/node/feed",               # Blognone (tech)
]

# ============================================================
# 4. STRATEGY MODE
#    เลือก 1 จาก: risk_averse / growth_focused /
#                 stability_first / efficiency_mode
# ============================================================
STRATEGY_MODE = "growth_focused"

# ============================================================
# 5. SIGNAL DETECTION SETTINGS
# ============================================================

# % การเปลี่ยนแปลงขั้นต่ำที่ถือว่า "มีนัยสำคัญ"
SIGNAL_THRESHOLD_PCT = 20.0

# จำนวนวันย้อนหลังสำหรับคำนวณ baseline
BASELINE_DAYS = 7

# ============================================================
# 6. REPORT SETTINGS
# ============================================================

# โฟลเดอร์ที่เก็บ HTML report
REPORT_OUTPUT_DIR = "reports/"

# ภาษาของ report (ส่งให้ Gemini ใช้)
REPORT_LANGUAGE = "Thai"

# ============================================================
# 7. GEMINI API
# ============================================================

# ใส่ API key ที่นี่ หรือใช้ environment variable
# แนะนำ: ใช้ .env file และ python-dotenv
# GEMINI_API_KEY = "your-api-key-here"

import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

GEMINI_MODEL = "gemini-2.5-flash"

# ============================================================
# 8. SCHEDULE (สำหรับ auto-run)
# ============================================================

# รันทุกวันกี่โมง (24hr format)
SCHEDULE_HOUR = 8    # 08:00 น.
SCHEDULE_MINUTE = 0

# ============================================================
# 9. DATABASE
# ============================================================
DB_PATH = "data/signals.db"
