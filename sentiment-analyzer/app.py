from flask import Flask, render_template, request, flash
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = 'Bhanu12'

# API Key Configuration

api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyCa0Kk2SxpICxznwdtXSWD9KZtnUhzGvPw")
print("Using API Key:", api_key[:10], "...")
genai.configure(api_key=api_key)

# ✅ Test Gemini API Access Immediately
try:
    test_model = genai.GenerativeModel("gemini-pro")  # Use gemini-pro instead of flash
    test_response = test_model.generate_content("Say Hello", request_options={"timeout": 30})
    print("Gemini API Test Success ✅:", test_response.text)
except Exception as e:
    print("Gemini API Test Failed ❌:", e)

# ✅ Initialize the actual model used by the app
model = None
try:
    model = genai.GenerativeModel("gemini-pro")  # Also use gemini-pro here
except Exception as e:
    print(f"Error configuring Gemini API or initializing model: {e}")
    model = None


@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    key_phrases = ""
    summary = ""
    text_input = ""

    if request.method == "POST":
        text_input = request.form["text"]

        if not text_input.strip():
            flash("Please enter some text to analyze.", "warning")
            return render_template("index.html", sentiment=sentiment, key_phrases=key_phrases, summary=summary, text_input=text_input)

        if not model:
            flash("AI model is not configured. Please ensure your API key is valid.", "danger")
            return render_template("index.html", sentiment=sentiment, key_phrases=key_phrases, summary=summary, text_input=text_input)

        try:
            # Sentiment Analysis
            sentiment_prompt = f"Analyze the sentiment of this text, regardless of its language: '{text_input}'. Respond with one word only in English: Positive, Negative, or Neutral."
            sentiment_response = model.generate_content(sentiment_prompt, request_options={"timeout": 30})
            sentiment = sentiment_response.text.strip()
            if sentiment.lower() not in ["positive", "negative", "neutral"]:
                sentiment = "Neutral"

            # Key Phrase Extraction
            keywords_prompt = f"Extract up to 5 key phrases from the following text, regardless of its language. The extracted key phrases MUST be in English: '{text_input}'. List them, separated by commas."
            keywords_response = model.generate_content(keywords_prompt, request_options={"timeout": 30})
            key_phrases = keywords_response.text.strip()
            if key_phrases.lower() == "none" or not key_phrases:
                key_phrases = "No specific key phrases identified."

            # Text Summarization
            summary_prompt = f"Summarize the following text, regardless of its language, in 2-3 concise sentences: '{text_input}'"
            summary_response = model.generate_content(summary_prompt, request_options={"timeout": 30})
            summary = summary_response.text.strip()

        except Exception as e:
            sentiment = "Error"
            key_phrases = "Error during extraction."
            summary = "Error during summarization."
            print(f"Error during AI analysis: {e}")
            flash("An error occurred during analysis.", "danger")

    return render_template("index.html", sentiment=sentiment, key_phrases=key_phrases, summary=summary, text_input=text_input)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
