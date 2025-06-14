from flask import Flask, render_template, request, flash
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()  # Loads environment variables from the .env

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")
print("✅ Gemini model initialized!")

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    key_phrases = ""
    summary = ""
    text_input = ""

    if request.method == "POST":
        text_input = request.form.get("user_input", "")

        try:
            prompt = f"""Analyze the following text and return a JSON with sentiment, key_phrases, and summary:

{text_input}

Respond in **strict JSON format only** like this:
{{
  "sentiment": "positive | negative | neutral",
  "key_phrases": ["phrase1", "phrase2"],
  "summary": "short summary"
}}"""

            response = model.generate_content(prompt)
            output = response.text.strip()
            print("[DEBUG] model output:", output)

            # Extract JSON from model output
            match = re.search(r"\{.*\}", output, re.DOTALL)
            if match:
                json_str = match.group(0)
                data = json.loads(json_str)

                sentiment = data.get("sentiment", "Error").capitalize()
                key_phrases = ", ".join(data.get("key_phrases", []))
                summary = data.get("summary", "Error")
            else:
                raise ValueError("Invalid JSON format returned by model.")

        except Exception as e:
            print("❌ Processing error:", e, output)
            sentiment = "Error"
            key_phrases = "Error"
            summary = "Error"
            flash("An error occurred. Check logs or API key.", "danger")

    return render_template(
        "index.html",
        sentiment=sentiment,
        key_phrases=key_phrases,
        summary=summary,
        text_input=text_input
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
