# 🧠 AIE — Adaptive Intelligence Engine

> **Automated Market Signal Detection & AI-Powered Business Intelligence**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![OpenRouter](https://img.shields.io/badge/AI-OpenRouter-ff6b35)
![Status](https://img.shields.io/badge/Status-Experimental-yellow)

AIE (Adaptive Intelligence Engine) is an experimental data intelligence pipeline designed to automatically detect meaningful market signals and transform fragmented external data into structured business insights.

Market monitoring is typically manual and reactive. Important signals are often discovered *after* market sentiment has already shifted. This project was built to answer a core question:

> **Can early market signals be detected automatically — before humans notice them?**

---

## 📋 Table of Contents

- [Project Goal](#-project-goal)
- [Architecture](#️-how-it-works-architecture)
- [Design Philosophy](#-design-philosophy)
- [Initial Use Case](#-initial-use-case--energy-sector)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Seamless Scalability](#-seamless-scalability-change-industries-instantly)
- [Tech Stack](#-tech-stack)
- [Project Outcomes](#-project-outcomes)
- [Sample Output](#-sample-output)
- [Disclaimer](#-disclaimer)

---

## 🎯 Project Goal

The objective of AIE is to simulate an **automated intelligence analyst** capable of:

- Continuously monitoring external market signals
- Detecting statistically significant behavioral changes
- Converting raw information into structured insights
- Producing decision-ready reports automatically

Instead of replacing analysts, the system **reduces monitoring overhead** and highlights where human attention should focus.

---

## ⚙️ How It Works (Architecture)

The system automates the full intelligence pipeline, separating data collection, analysis, and decision logic into independent layers:

| # | Layer | File | Responsibility |
|---|---|---|---|
| 1 | **Data Source** | `plugins/google_trends.py`<br>`plugins/news_rss.py` | Collects search volume from Google Trends and news from RSS feeds |
| 2 | **Normalization** | `pipeline/normalizer.py` | Converts heterogeneous data into a Universal Schema and stores it in SQLite |
| 3 | **Signal Detection** | `pipeline/signal_detector.py` | Compares current activity against a rolling baseline to identify abnormal deviations |
| 4 | **Insight AI** | `engine/insight_ai.py` | Interprets detected signals using OpenRouter AI (LLM) |
| 5 | **Strategy Engine** | `engine/strategy.py` | Adjusts recommendations based on active operating mode |
| 6 | **Decision Output** | `output/report_builder.py` | Generates a daily decision-ready HTML intelligence report |

**Pipeline Flow:**

```
plugins/          →   pipeline/          →   engine/         →   output/
(collect)             (normalize &            (reason &           (report)
                       detect signals)         strategize)
```

---

## 🧠 Design Philosophy

AIE follows five engineering principles:

**1. Separation of Concerns**
Each layer performs one responsibility only — collection, normalization, reasoning, or reporting — allowing independent evolution.

**2. Signal Over Data**
Raw data is noisy. The system prioritizes detecting *change* rather than storing large volumes of information.

**3. Configuration Over Hardcoding**
Industries, brands, and monitoring targets are defined via configuration instead of code changes.

**4. Analyst-Centric Output**
Outputs are designed as readable intelligence reports rather than raw dashboards.

**5. Lightweight Intelligence Architecture**
Runs locally using simple components (Python + SQLite) while demonstrating scalable architectural concepts.

---

## 🧪 Initial Use Case — Energy Sector

The first implementation monitors Thailand's energy ecosystem:

- **Brands:** PTT, SPRC, BAFS, Bangchak, Thai Oil
- **Keywords:** Crude oil prices, OPEC, Middle East conflict

Energy markets were selected due to their sensitivity to geopolitical and macroeconomic sentiment.

The system compares current activity against a **7-day rolling baseline** and highlights statistically significant deviations.

### Signal Types

| Signal | Meaning | Criteria |
|---|---|---|
| 🔴 `ACCELERATION` | Unusual spike in interest | > +20% from baseline |
| 🔵 `DECLINE` | Continuous drop in interest | < −20% from baseline |
| 🟡 `ANOMALY` | Deviation from normal patterns | Outside ± threshold |

---

## 📁 Project Structure

```
AIE-Pulse-Meridian/
├── plugins/
│   ├── google_trends.py      # Google Trends data collector
│   └── news_rss.py           # RSS news feed collector
├── pipeline/
│   ├── normalizer.py         # Universal schema + SQLite storage
│   └── signal_detector.py    # Rolling baseline & deviation detection
├── engine/
│   ├── insight_ai.py         # LLM-powered signal interpretation
│   └── strategy.py           # Operating mode & recommendation logic
├── output/
│   └── report_builder.py     # HTML report generator
├── sample_output/            # Example generated reports
├── config.py                 # Use case configuration
├── main.py                   # Pipeline entry point
├── requirements.txt
└── .env                      # API key (not committed)
```

---

## 🔧 Prerequisites

- Python 3.11+
- A free [OpenRouter](https://openrouter.ai) API key (no credit card required)
- Internet connection for data collection

---

## 🚀 Quick Start

### 1️⃣ Clone and Install

```bash
git clone https://github.com/adulsaa-q/AIE-Pulse-Meridian.git
cd AIE-Pulse-Meridian
pip install -r requirements.txt
```

### 2️⃣ Setup Environment

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your-key-here
```

> Free API keys available at [https://openrouter.ai](https://openrouter.ai) — no credit card required.

### 3️⃣ Configure Use Case (`config.py`)

```python
USE_CASE = "energy_sector"

BRANDS = [
    "PTT",
    "SPRC",
    "BAFS",
    "บางจาก",
    "ไทยออยล์"
]

KEYWORDS = [
    "ราคาน้ำมันดิบ",
    "OPEC",
    "สงครามตะวันออกกลาง"
]
```

### 4️⃣ Run the Pipeline

```bash
python main.py
```

The generated HTML report will be saved in the `reports/` folder and can be opened directly in any web browser.

---

## 🧩 Seamless Scalability (Change Industries Instantly)

The system is **not hardcoded** to any specific industry.

Changing sectors only requires updating `config.py`. Databases and baselines are automatically separated per use case.

```python
# Banking Sector
USE_CASE = "banking"
BRANDS   = ["SCB", "Kbank", "TTB"]
KEYWORDS = ["ดอกเบี้ย", "แบงก์ชาติ"]
```

```python
# Food Delivery
USE_CASE = "food_delivery"
BRANDS   = ["Grab", "LINE MAN", "foodpanda"]
KEYWORDS = ["ส่งอาหาร", "โปรโมชั่น"]
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core runtime |
| pandas | Data transformation |
| pytrends | Google Trends API wrapper |
| feedparser | RSS news collection |
| SQLite | Lightweight local storage |
| OpenRouter AI | LLM inference for signal interpretation |

Designed to run **locally** with minimal infrastructure requirements.

---

## 📊 Project Outcomes

This project demonstrates how an automated pipeline can:

- ✅ Detect abnormal market attention early
- ✅ Reduce manual monitoring workflows
- ✅ Transform external signals into structured intelligence
- ✅ Generate analyst-style insights automatically
- ✅ Produce daily decision-support reports without human intervention

---

## 📄 Sample Output

View generated reports inside:

```
sample_output/
```

Reports are exported as **standalone HTML files** for easy viewing and sharing — no additional software required.

---

## ⚠️ Disclaimer

AIE is an **experimental research project** built for learning and portfolio purposes. Signal outputs should not be used as the sole basis for investment or business decisions. Always validate insights with additional sources and professional judgment.

---

*Built with curiosity. Powered by data.*
