# AIE — Adaptive Intelligence Engine
## System Architecture

---

## Overview

AIE แปลง raw data → signal → insight → strategy → decision recommendation
โดยไม่ผูกกับอุตสาหกรรมใด ทำงานได้กับทุก business domain

```
DATA → SIGNAL → INSIGHT → STRATEGY → DECISION
```

---

## 6-Layer Architecture

### Layer 1: Data Source Plugin
**ไฟล์:** `plugins/`
**หน้าที่:** ดึงข้อมูลจากแหล่งภายนอก และแปลงให้อยู่ใน Universal Schema
**Plugin ที่มีใน MVP:**
- `google_trends.py` — ดึง search volume จาก Google Trends (pytrends)
- `news_rss.py` — ดึงข่าวจาก RSS Feed (feedparser)

**กฎสำคัญ:** ทุก plugin ต้อง output เป็น Universal Schema เท่านั้น

---

### Layer 2: Data Normalization
**ไฟล์:** `pipeline/normalizer.py`
**หน้าที่:** รับข้อมูลจากทุก plugin → clean → เก็บลง SQLite
**กฎสำคัญ:** ห้ามมี field นอกเหนือจาก Universal Schema

---

### Layer 3: Signal Detection
**ไฟล์:** `pipeline/signal_detector.py`
**หน้าที่:** เปรียบเทียบข้อมูลกับ historical baseline → ตรวจจับ signal ที่มีนัยสำคัญ
**Signal types:**
- `ANOMALY` — ค่าเบี่ยงเบนผิดปกติจาก baseline
- `ACCELERATION` — เพิ่มขึ้นเร็วผิดปกติ
- `DECLINE` — ลดลงต่อเนื่อง
- `VOLATILITY` — ผันผวนสูงผิดปกติ

---

### Layer 4: Insight Reasoning AI
**ไฟล์:** `engine/insight_ai.py`
**หน้าที่:** ส่ง signal ให้ Gemini API วิเคราะห์ และ output insight ตาม framework
**Insight Framework (บังคับครบทุกข้อ):**
1. WHAT CHANGED
2. WHY IT MATTERS
3. POSSIBLE DRIVERS
4. BUSINESS IMPACT
5. CONFIDENCE LEVEL

**กฎสำคัญ:** AI ห้าม reason นอกเหนือจากข้อมูลที่ส่งไป (no hallucination)

---

### Layer 5: Strategy Engine
**ไฟล์:** `engine/strategy.py`
**หน้าที่:** ปรับ recommendation ตาม strategy mode ขององค์กร
**Strategy modes:**
- `risk_averse` → เน้น risk mitigation
- `growth_focused` → เน้น opportunity (MVP default)
- `stability_first` → ลด volatility
- `efficiency_mode` → optimize resource

---

### Layer 6: Decision Output Layer
**ไฟล์:** `output/report_builder.py`
**หน้าที่:** สร้าง HTML report รายวัน พร้อม insight และ recommended action
**Output:** ไฟล์ HTML ใน `reports/` พร้อมเปิดบน browser ได้ทันที

---

## Folder Structure

```
aie/
├── plugins/
│   ├── google_trends.py
│   └── news_rss.py
├── pipeline/
│   ├── normalizer.py
│   └── signal_detector.py
├── engine/
│   ├── insight_ai.py
│   └── strategy.py
├── output/
│   └── report_builder.py
├── data/
│   └── signals.db
├── reports/
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Data Flow

```
config.py (brands, keywords, strategy_mode)
    ↓
plugins/ → ดึงข้อมูลจาก Google Trends + RSS
    ↓
pipeline/normalizer.py → Universal Schema → signals.db (SQLite)
    ↓
pipeline/signal_detector.py → เปรียบเทียบ baseline → ระบุ signal type
    ↓
engine/insight_ai.py → Gemini API → WHAT/WHY/IMPACT/CONFIDENCE
    ↓
engine/strategy.py → ปรับตาม strategy mode
    ↓
output/report_builder.py → HTML report → reports/YYYY-MM-DD.html
```

---

## MVP Scope (สัปดาห์ที่ 1-2)

| Layer | MVP Status |
|---|---|
| Data Source Plugin | ✅ Google Trends + RSS Feed |
| Data Normalization | ✅ Universal Schema + SQLite |
| Signal Detection | ✅ ANOMALY, DECLINE, ACCELERATION |
| Insight Reasoning AI | ✅ Gemini API (free tier) |
| Strategy Engine | ✅ growth_focused mode |
| Decision Output | ✅ HTML report |

---

## Tech Stack

| Tool | Purpose | Cost |
|---|---|---|
| Python 3.11+ | Core language | ฟรี |
| pytrends | Google Trends API | ฟรี |
| feedparser | RSS Feed parser | ฟรี |
| SQLite | Local database | ฟรี (built-in) |
| Google Gemini API | AI insight reasoning | ฟรี (15 req/min) |
| APScheduler | Task scheduling | ฟรี |

**ค่าใช้จ่ายรวม: 0 บาท**
