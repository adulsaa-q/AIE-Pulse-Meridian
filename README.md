# 🧠 AIE — Adaptive Intelligence Engine

> Automated Market Signal Detection & AI-Powered Business Intelligence

ระบบ pipeline อัตโนมัติที่ดึงข้อมูลจากหลายแหล่ง ตรวจจับสัญญาณที่มีนัยสำคัญ และให้ AI วิเคราะห์ insight เพื่อสนับสนุนการตัดสินใจเชิงธุรกิจ

---

## Use Case แรก — Energy Sector

ติดตาม **PTT · SPRC · BAFS · บางจาก · ไทยออยล์** พร้อม keyword ตลาด เช่น ราคาน้ำมันดิบ และ OPEC โดยเปรียบเทียบกับ baseline 7 วันย้อนหลัง แล้วสรุปออกมาเป็น HTML report รายวัน

---

## Architecture
```
plugins/   →   pipeline/   →   engine/   →   output/
(collect)      (normalize)     (AI)          (report)
```

| # | Layer | ไฟล์ | หน้าที่ |
|---|---|---|---|
| 1 | Data Source | `plugins/google_trends.py` | Search volume จาก Google Trends |
| 1 | Data Source | `plugins/news_rss.py` | ข่าวจาก RSS Feed |
| 2 | Normalization | `pipeline/normalizer.py` | Universal Schema → SQLite |
| 3 | Signal Detection | `pipeline/signal_detector.py` | เปรียบเทียบ baseline → signal type |
| 4 | Insight AI | `engine/insight_ai.py` | วิเคราะห์ผ่าน OpenRouter |
| 5 | Strategy Engine | `engine/strategy.py` | ปรับ recommendation ตาม mode |
| 6 | Decision Output | `output/report_builder.py` | สร้าง HTML report |

---

## Quick Start

**1. Clone และติดตั้ง**
```bash
git clone https://github.com/adulsaa-q/AIE-Pulse-Meridian.git
cd AIE-Pulse-Meridian
pip install -r requirements.txt
```

**2. สร้างไฟล์ `.env`**
```
OPENROUTER_API_KEY=your-key-here
```
สมัคร API key ฟรีได้ที่ [openrouter.ai](https://openrouter.ai) — ไม่ต้องบัตรเครดิต

**3. ตั้งค่า Use Case ใน `config.py`**
```python
USE_CASE = "energy_sector"
BRANDS   = ["PTT", "SPRC", "BAFS", "บางจาก", "ไทยออยล์"]
KEYWORDS = ["ราคาน้ำมันดิบ", "OPEC", "สงครามตะวันออกกลาง"]
```

**4. รัน**
```bash
python main.py
```

Report จะถูกบันทึกไว้ใน `reports/` เปิดด้วย browser ได้เลย

---

## Signal Types

| Signal | ความหมาย | เกณฑ์ |
|---|---|---|
| `ACCELERATION` | ความสนใจพุ่งขึ้นผิดปกติ | > +20% จาก baseline |
| `DECLINE` | ความสนใจลดลงต่อเนื่อง | < −20% จาก baseline |
| `ANOMALY` | เบี่ยงเบนจากปกติ | ± นอก threshold |

---

## เปลี่ยน Use Case ได้ทันที

ระบบไม่ผูกกับอุตสาหกรรมใด — แค่แก้ `config.py` แล้วรันใหม่ database จะแยกกันอัตโนมัติ
```python
# Banking
USE_CASE = "banking"
BRANDS   = ["SCB", "Kbank", "TTB"]
KEYWORDS = ["ดอกเบี้ย", "แบงก์ชาติ"]

# Food Delivery
USE_CASE = "food_delivery"
BRANDS   = ["Grab", "LINE MAN", "foodpanda"]
KEYWORDS = ["ส่งอาหาร", "โปรโมชั่น"]
```

---

## Tech Stack

`Python 3.11` · `pytrends` · `feedparser` · `pandas` · `SQLite` · `OpenRouter AI`

**ค่าใช้จ่าย: 0 บาท**

---

## Sample Output

ดูตัวอย่าง report ได้ที่ [`sample_output/`](sample_output/)

---

## Author

**Q** — Data Analyst · [GitHub](https://github.com/adulsaa-q)