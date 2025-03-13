import streamlit as st
import openai
import wikipedia

# Set your OpenAI API key
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def ask_llm(question):
    """Fetches step-by-step academic answers from GPT-4."""
    prompt = f"Explain this academic question step-by-step with sources: {question}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an academic tutor."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error fetching response: {str(e)}"

def get_wikipedia_summary(query):
    """Fetches a brief summary from Wikipedia."""
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "No Wikipedia reference found."

# Streamlit UI
st.set_page_config(page_title="Doubt Solver Bot", page_icon="📚", layout="centered")
st.title("📚 Doubt Solver Bot")
st.write("Ask your academic questions and get detailed answers!")

question = st.text_area("Enter your question:")
if st.button("Solve"):
    if question:
        with st.spinner("Solving your doubt..."):
            answer = ask_llm(question)
            source = get_wikipedia_summary(question)
            
            st.subheader("📖 Answer:")
            st.write(answer)
            
            st.subheader("🔗 Sources:")
            st.write(source)
    else:
        st.warning("Please enter a question.")
