from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# UI setup
st.set_page_config(page_title="QueryCraft: Text-to-SQL", layout="wide")
st.title("🔮 QueryCraft: Text-to-SQL Converter")

# Optional: Display an icon
icon_path = "images/icon.png"
if os.path.exists(icon_path):
    st.image(Image.open(icon_path), width=100)

st.markdown("Enter your question in English, and QueryCraft will generate the SQL query for you.")

# User input
user_input = st.text_area("Your question:", height=100)

# Prompt template
PROMPT = """
You are an expert SQL developer.
Convert the following English request into an optimized SQL query.
Return only the SQL code, nothing else.

Request: {query}
"""

def get_sql_from_gemini(nl_query):
    prompt =  f"""Convert this English to SQL:
    {nl_query}
    Rules:
    1. Use ANSI SQL
    2. Return ONLY SQL code"""
    response = model.generate_content(prompt)
    return response.text.strip()

if st.button("Generate SQL"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating SQL..."):
            sql_query = get_sql_from_gemini(user_input)
            st.subheader("Generated SQL Query")
            st.code(sql_query, language="sql")
