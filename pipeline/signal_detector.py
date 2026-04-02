import sqlite3
import pandas as pd
import config

def detect_signals() -> list[dict]:
    """
    ตรวจจับ signals โดยเปรียบเทียบค่าวันนี้กับค่าเฉลี่ย BASELINE_DAYS วันก่อนหน้า
    ANOMALY = การเปลี่ยนแปลงสุดขีด (>= 3 เท่าของ threshold)
    """
    days_needed = config.BASELINE_DAYS + 1
    with sqlite3.connect(config.DB_PATH) as conn:
        df = pd.read_sql(
            f"SELECT * FROM signals WHERE date >= date('now', '-{days_needed} days') ORDER BY date ASC",
            conn
        )

    signals = []
    for (entity, metric), group in df.groupby(["entity", "metric_name"]):
        if len(group) < 2:
            continue

        # ค่าเฉลี่ย baseline: ย้อนหลังสูงสุด BASELINE_DAYS วัน (ไม่รวมวันนี้)
        history = group.iloc[:-1].tail(config.BASELINE_DAYS)
        baseline = history["metric_value"].mean()
        current = group["metric_value"].iloc[-1]

        if baseline == 0:
            continue

        pct_change = (current - baseline) / baseline * 100

        if abs(pct_change) < config.SIGNAL_THRESHOLD_PCT:
            continue

        # จำแนกประเภท signal — ANOMALY คือการเปลี่ยนแปลงสุดขีด (>= 3x threshold)
        if abs(pct_change) >= config.SIGNAL_THRESHOLD_PCT * 3:
            signal_type = "ANOMALY"
        elif pct_change > 0:
            signal_type = "ACCELERATION"
        else:
            signal_type = "DECLINE"

        signals.append({
            "entity": entity,
            "metric_name": metric,
            "signal_type": signal_type,
            "current_value": current,
            "baseline": round(baseline, 2),
            "pct_change": round(pct_change, 2)
        })

    return signals
