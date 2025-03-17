import os
import streamlit as st
import google.generativeai as genai
import wikipedia
from dotenv import load_dotenv

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Use the correct Gemini model
MODEL_NAME = "gemini-1.5-pro-latest"  # You can also try "gemini-2.0-pro-exp"

# Streamlit UI
st.title("📚 Doubt Solver Bot (Gemini AI)")
st.write("Ask any academic question and get a detailed, step-by-step solution!")

# User Input
question = st.text_input("Enter your question:")

if question:
    # Fetch Wikipedia Summary
    try:
        wiki_summary = wikipedia.summary(question, sentences=2)
    except:
        wiki_summary = "No Wikipedia data found."

    # Use Gemini AI for Answer
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(question)

    # Display Answer
    st.subheader("📌 Step-by-Step Solution")
    st.write(response.text)

    # Show Wikipedia Summary
    st.subheader("📖 Additional Context (Wikipedia)")
    st.write(wiki_summary)
