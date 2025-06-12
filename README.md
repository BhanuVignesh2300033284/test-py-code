# 💬 Advanced Sentiment Analyzer

The Advanced Sentiment Analyzer is a web-based Natural Language Processing (NLP) tool that performs three major tasks:

- **Sentiment Analysis** (Positive / Negative / Neutral)
- **Key Phrase Extraction**
- **Text Summarization**

It supports **multiple languages** including **English, Telugu, Hindi,  Japanese**, etc. It’s built using **Flask** for the backend and **Google Gemini API** for the AI-powered text analysis.

---

## 🔍 Features

- **Sentiment Detection**: Understand the emotional tone of the text.
- **Key Phrase Extraction**: Highlight the most important phrases in the text.
- **Summarization**: Get a short summary of long content in a few seconds.
- **Multilingual Support**: Works with texts written in regional and foreign languages.
- **Simple UI**: Clean and easy-to-use interface built with HTML and CSS.

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS  
- **Backend**: Flask (Python)  
- **AI Model**: Google Gemini 1.5 Flash (via Google Generative AI API)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/advanced-sentiment-analyzer.git
cd advanced-sentiment-analyzer

2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the App
check your in the right file cd sentiment-analyzer
python app.py
Visit http://localhost:5000 in your browser.



🔐 API Key Setup
Replace the genai.configure() line in app.py with your own Google AI Studio API key:


genai.configure(api_key="your-api-key") 



📌 Example Input
Input:
"The movie had amazing visuals but lacked a good story. The soundtrack was beautiful though."

Output:
Sentiment: Neutral
Key Phrases: amazing visuals, good story, soundtrack
Summary: The movie had stunning visuals and a beautiful soundtrack, but the story was weak.



📈 Future Enhancements:

Add user authentication
Export analysis to PDF or text file
Use a database to store previous results
Add charts for better visualization