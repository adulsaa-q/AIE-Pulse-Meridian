# ✅ ถูก — อยู่นอก function
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import config

load_dotenv()

client = OpenAI(
    api_key=config.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def analyze(signals: list[dict]) -> list[dict]:
    """รับ signals แล้วส่งให้ AI วิเคราะห์"""
    insights = []
    for signal in signals:
        prompt = f"""
You are a senior business analyst. Analyze this market signal:

Entity: {signal['entity']}
Signal Type: {signal['signal_type']}
Current Value: {signal['current_value']}
Baseline (7-day avg): {signal['baseline']}
% Change: {signal['pct_change']}%

Respond in Thai language with exactly these 5 sections:
1. WHAT CHANGED: What happened
2. WHY IT MATTERS: Why this is important
3. POSSIBLE DRIVERS: What caused this
4. BUSINESS IMPACT: How this affects the business
5. CONFIDENCE LEVEL: How confident (0-100%)
"""
        response = client.chat.completions.create(
            model=config.OPENROUTER_MODEL,
            messages=[{"rel_role": "user", "content": prompt}]
        )
        insight_text = response.choices[0].message.content
        insights.append({
            "entity":      signal["entity"],
            "metric_name": signal["metric_name"],
            "signal_type": signal["signal_type"],
            "insight":     insight_text,
            "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return insights