import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key="AIzaSyDPyhhkbp4OieQKbS15OAWiUH5txpJ8epI")

print("Listing available models that support generateContent:")
try:
    found_gemini_pro = False
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(f"  Model Name: {m.name}")
            if m.name == "models/gemini-pro":
                found_gemini_pro = True
    if not found_gemini_pro:
        print("\n'models/gemini-pro' not found. Check API access or use another supported model.")
except Exception as e:
    print(f"Error listing models: {e}")
