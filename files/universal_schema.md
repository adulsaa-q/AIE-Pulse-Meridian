# AIE — Universal Data Schema

---

## หลักการ

ทุก data source ใน AIE ต้องแปลงเป็น schema นี้ก่อนเข้า pipeline
ห้ามมี field เพิ่มเติมนอกเหนือจากนี้ใน normalization layer

---

## Schema Fields

| Field | Type | Description | ตัวอย่าง |
|---|---|---|---|
| `date` | datetime | วันเวลาที่เก็บข้อมูล | `2026-03-28 09:00:00` |
| `entity` | string | แบรนด์ หรือ keyword ที่ track | `"Shopee"`, `"ประกันชีวิต"` |
| `metric_name` | string | ชื่อ metric ที่วัด | `"search_volume"`, `"mention_count"` |
| `metric_value` | float | ค่าของ metric | `78.5`, `12.0` |
| `dimension` | string | บริบทเพิ่มเติม (optional) | `"Thailand"`, `"tech_news"` |
| `source` | string | แหล่งที่มาของข้อมูล | `"google_trends"`, `"rss_feed"` |

---

## ตัวอย่าง Records

```
date,                entity,   metric_name,    metric_value, dimension,  source
2026-03-28 09:00:00, Shopee,   search_volume,  78.5,         Thailand,   google_trends
2026-03-28 09:00:00, Lazada,   search_volume,  91.2,         Thailand,   google_trends
2026-03-28 09:00:00, Shopee,   mention_count,  12.0,         tech_news,  rss_feed
2026-03-28 09:00:00, Lazada,   mention_count,  3.0,          tech_news,  rss_feed
```

---

## SQLite Table Definition

```sql
CREATE TABLE IF NOT EXISTS signals (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    date         DATETIME NOT NULL,
    entity       TEXT NOT NULL,
    metric_name  TEXT NOT NULL,
    metric_value REAL NOT NULL,
    dimension    TEXT,
    source       TEXT NOT NULL
);

-- Index สำหรับ query ตาม entity และ date
CREATE INDEX IF NOT EXISTS idx_entity_date
ON signals (entity, date);
```

---

## Metric Names ที่ใช้ใน MVP

| metric_name | มาจาก source | หน่วย |
|---|---|---|
| `search_volume` | google_trends | 0–100 (relative) |
| `mention_count` | rss_feed | จำนวนครั้ง |
| `sentiment_score` | rss_feed + AI | -1.0 ถึง 1.0 |

---

## กฎสำคัญ

1. **ทุก plugin ต้อง return list of dict** ที่มี 6 fields นี้ครบ
2. **`metric_value` ต้องเป็น float เสมอ** — ห้ามเป็น string
3. **`date` ต้องเป็น ISO format** — `YYYY-MM-DD HH:MM:SS`
4. **`dimension` ใส่ `""` ได้ถ้าไม่มีข้อมูล** — ห้าม None/null
5. **`entity` ต้องตรงกับ `BRANDS` ใน config.py** — case-sensitive

---

## Python Template สำหรับ Plugin

```python
def collect() -> list[dict]:
    """
    ทุก plugin ต้อง implement function นี้
    และ return records ที่ตรงกับ Universal Schema เท่านั้น
    """
    records = []
    records.append({
        "date":         "2026-03-28 09:00:00",  # str ISO format
        "entity":       "Shopee",                # ตรงกับ config.BRANDS
        "metric_name":  "search_volume",         # lowercase_underscore
        "metric_value": 78.5,                    # float เสมอ
        "dimension":    "Thailand",              # "" ถ้าไม่มี
        "source":       "google_trends"          # ชื่อ plugin
    })
    return records
```
