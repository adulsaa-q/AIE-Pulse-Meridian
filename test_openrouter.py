from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="stepfun/step-3.5-flash:free",
    messages=[{"role": "user", "content": "สวัสดี ตอบสั้นๆ ได้เลย"}]
)

print(response.choices[0].message.content)