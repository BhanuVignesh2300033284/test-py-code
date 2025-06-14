import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """
Respond only in JSON:

{
  "sentiment": "Positive/Negative/Neutral",
  "key_phrases": ["..."],
  "summary": "..."
}

Analyze this:
"The rooster crowed cockadoodledoo to awaken everyone on the farm."
"""

try:
    response = model.generate_content(prompt)
    print("Response:")
    print(response.text)
except Exception as e:
    print("❌ Error:", e)
