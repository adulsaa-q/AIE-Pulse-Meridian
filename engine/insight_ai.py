from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import config

load_dotenv()

client = OpenAI(
    api_key=config.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

def analyze(signals: list[dict]) -> list[dict]:
    """รับ signals แล้วส่งให้ AI วิเคราะห์แบบกระชับ (Executive Summary)"""
    
    insights = []

    for signal in signals:

        # ปรับ Prompt ใหม่ให้ AI ตอบสั้น กระชับ เป็นภาษาไทย และใช้ Bullet points
        prompt = f"""
คุณคือนักวิเคราะห์ธุรกิจระดับ Senior หน้าที่ของคุณคือสรุปข้อมูลต่อไปนี้ให้ผู้บริหารอ่าน
ข้อบังคับ:
1. ตอบเป็น 'ภาษาไทย' เท่านั้น
2. ต้องเขียนให้ 'สั้น กระชับ ตรงประเด็น' (หัวข้อละไม่เกิน 2-3 บรรทัด)
3. ห้ามพิมพ์ข้อความเกริ่นนำหรือคำลงท้ายใดๆ ทั้งสิ้น เริ่มต้นที่ข้อ 1 ทันที

ข้อมูลที่ตรวจพบ:
- สิ่งที่จับสัญญาณได้ (Entity): {signal['entity']}
- แหล่งที่มา (Metric): {signal['metric_name']}
- ประเภทสัญญาณ: {signal['signal_type']}
- ค่าปัจจุบัน: {signal['current_value']} (ค่าเฉลี่ย 7 วัน: {signal['baseline']})
- อัตราการเปลี่ยนแปลง: {signal['pct_change']}%

กรุณาตอบตามโครงสร้าง 5 ข้อนี้อย่างเคร่งครัด:
1. เกิดอะไรขึ้น: (สรุปสั้นๆ ว่าตัวเลขเปลี่ยนไปอย่างไร)
2. ทำไมถึงสำคัญ: (Impact ระยะสั้น)
3. สาเหตุที่เป็นไปได้: (ยกตัวอย่าง 2-3 ข้อสั้นๆ)
4. ผลกระทบทางธุรกิจ: (ส่งผลดีหรือเสียต่อบริษัทอย่างไร)
5. ความมั่นใจ: (0-100% พร้อมเหตุผลสั้นๆ 1 ประโยค)
"""

        try:
            # ---- OpenRouter API call ----
            response = client.chat.completions.create(
                model=config.OPENROUTER_MODEL,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                extra_headers={
                    "HTTP-Referer": "http://localhost",
                    "X-Title": "AIE Pulse Meridian"
                }
            )

            insight_text = response.choices[0].message.content.strip()

        except Exception as e:
            insight_text = f"ไม่สามารถวิเคราะห์ข้อมูลได้เนื่องจากข้อผิดพลาดของ API: {e}"

        # ส่งค่า pct_change และ metric_name กลับไปให้ครบ เพื่อให้ report_builder นำไปใช้ต่อได้
        insights.append({
            "entity": signal["entity"],
            "metric_name": signal["metric_name"],
            "signal_type": signal["signal_type"],
            "pct_change": signal["pct_change"], # แก้ไขปัญหา N/A%
            "insight": insight_text,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return insights