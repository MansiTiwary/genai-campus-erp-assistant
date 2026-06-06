import google.generativeai as genai

API_KEY = "AQ.Ab8RN6LhoA-3Uw778DYo3BAHQLf69DofCw2hRt-4qJNebO-zFg"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI service error: {str(e)}"
