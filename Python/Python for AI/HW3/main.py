import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API KEY =", api_key)

if not api_key:
    raise ValueError("Переменная окружение GEMINI_API_KEY не найдена.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")


prompt = "Предложи лучший телефон в бюджете 200$"

response = model.generate_content(prompt)

print(response.text)