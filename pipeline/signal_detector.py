import sqlite3
import pandas as pd
import config

def detect_signals() -> list[dict]:
    """
    Detect signals from other plugins using a 7-day baseline in SQLite.
    """
    conn = sqlite3.connect(config.DB_PATH)
    df = pd.read_sql("SELECT * FROM signals ORDER BY date ASC", conn)
    conn.close()
    signals = []
    for (entity, metric), group in df.groupby(["entity", "metric_name"]):
        if len(group) < 2:
            continue
        # AVG of last 7 days excluding today
        baseline = group["metric_value"].iloc[:-1].mean()
        #current value
        current = group["metric_value"].iloc[-1]
        #prevent division by zero
        if baseline == 0:
            continue
        # calculate percentage change
        pct_change = (current - baseline) / baseline * 100
        if abs(pct_change) < config.SIGNAL_THRESHOLD_PCT:
            continue
        # Determine the type of signal
        if pct_change >= config.SIGNAL_THRESHOLD_PCT:
            signal_type = "ACCELERATION"
        elif pct_change <= -config.SIGNAL_THRESHOLD_PCT:
            signal_type = "DECLINE"
        else:
            signal_type = "ANOMALY"
            # Append signal to list
        signals.append({
            "entity": entity,
            "metric_name": metric,
            "signal_type": signal_type,
            "current_value": current,
            "baseline": baseline,
            "pct_change": round(pct_change, 2)
        })
    return signals
