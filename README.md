# 🧠 AIE — Adaptive Intelligence Engine

> **Automated Market Signal Detection & AI-Powered Business Intelligence**

ระบบ pipeline อัตโนมัติที่ดึงข้อมูลจากหลายแหล่ง ตรวจจับสัญญาณสำคัญ และให้ AI วิเคราะห์ insight เพื่อช่วยผู้บริหารตัดสินใจ

---

## 🎯 Use Case แรก — Energy Sector Intelligence

ติดตาม PTT, SPRC, BAFS, บางจาก, ไทยออยล์ และราคาน้ำมันดิบ โดยเปรียบเทียบกับ baseline 7 วันย้อนหลัง แล้วสรุป insight ออกมาเป็น HTML report รายวัน

---

## ⚙️ Architecture — 6 Layer Pipeline
```
Data Source Plugin  →  Normalization  →  Signal Detection
                                               ↓
Decision Output    ←  Strategy Engine  ←  Insight AI
```

| Layer | ไฟล์ | หน้าที่ |
|---|---|---|
| 1. Data Source | `plugins/` | ดึงข้อมูลจาก Google Trends + RSS Feed |
| 2. Normalization | `pipeline/normalizer.py` | แปลง → Universal Schema → SQLite |
| 3. Signal Detection | `pipeline/signal_detector.py` | เปรียบเทียบ baseline → ACCELERATION / DECLINE |
| 4. Insight AI | `engine/insight_ai.py` | ส่งให้ AI วิเคราะห์ผ่าน OpenRouter |
| 5. Strategy Engine | `engine/strategy.py` | ปรับ recommendation ตาม strategy mode |
| 6. Decision Output | `output/report_builder.py` | สร้าง HTML report |

---

## 🚀 Quick Start

### 1. Clone และติดตั้ง
```bash
git clone https://github.com/adulsaa-q/AIE-Pulse-Meridian.git
cd AIE-Pulse-Meridian
pip install -r requirements.txt
```

### 2. ตั้งค่า API Key

สร้างไฟล์ `.env` แล้วใส่
```
OPENROUTER_API_KEY=your-key-here
```

สมัคร API key ฟรีได้ที่ [openrouter.ai](https://openrouter.ai) ไม่ต้องบัตรเครดิต

### 3. ตั้งค่า Use Case

เปิด `config.py` แล้วแก้
```python
USE_CASE = "energy_sector"   # ชื่อ database
BRANDS   = ["PTT", "SPRC"]  # แบรนด์ที่ต้องการติดตาม
KEYWORDS = ["ราคาน้ำมัน"]   # keyword ตลาด
```

### 4. รันระบบ
```bash
python main.py
```

เปิด HTML report ที่สร้างขึ้นใน `reports/` ด้วย browser ได้เลย

---

## 📊 Signal Types

| Signal | ความหมาย | เกณฑ์ |
|---|---|---|
| ACCELERATION | ความสนใจพุ่งสูงขึ้น | > +20% จาก baseline |
| DECLINE | ความสนใจลดลง | < -20% จาก baseline |
| ANOMALY | ผิดปกติ | เบี่ยงเบนจาก baseline |

---

## 🛠️ Tech Stack

| Tool | หน้าที่ | ค่าใช้จ่าย |
|---|---|---|
| Python 3.11+ | Core language | ฟรี |
| pytrends | Google Trends API | ฟรี |
| feedparser | RSS Feed parser | ฟรี |
| SQLite | Local database | ฟรี |
| OpenRouter | AI API Gateway | ฟรี |
| pandas | Data processing | ฟรี |

**ค่าใช้จ่ายรวม: 0 บาท**

---

## 📁 Project Structure
```
AIE-Pulse-Meridian/
├── plugins/
│   ├── google_trends.py    # Layer 1: ดึง search volume
│   └── news_rss.py         # Layer 1: ดึงข่าวจาก RSS
├── pipeline/
│   ├── normalizer.py       # Layer 2: เก็บลง SQLite
│   └── signal_detector.py  # Layer 3: หา signals
├── engine/
│   ├── insight_ai.py       # Layer 4: AI วิเคราะห์
│   └── strategy.py         # Layer 5: ปรับ recommendation
├── output/
│   └── report_builder.py   # Layer 6: สร้าง HTML report
├── config.py               # ตั้งค่าทั้งระบบ
├── main.py                 # รันทุก layer ด้วยคำสั่งเดียว
└── requirements.txt
```

---

## 💡 เปลี่ยน Use Case ได้ทันที

ระบบนี้ไม่ผูกกับอุตสาหกรรมใด — แค่แก้ `config.py` บรรทัดเดียว
```python
# ติดตามธนาคาร
USE_CASE = "banking"
BRANDS   = ["SCB", "Kbank", "TTB"]

# ติดตาม Food Delivery
USE_CASE = "food_delivery"
BRANDS   = ["Grab", "LINE MAN", "foodpanda"]
```

แต่ละ Use Case จะมี database แยกกันอัตโนมัติ

---

## 👤 Author

**Q** — Data Analyst | [GitHub](https://github.com/adulsaa-q)