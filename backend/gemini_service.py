# pyrefly: ignore [missing-import]
import google.generativeai as genai

API_KEY = "AIzaSyC-fu7M1M-PpFO_JqTkHleYe2oM9XbA61g"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
