import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
