import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model & tokenizer
@st.cache_resource
def load_model():
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"  # You can change this to another model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    return model, tokenizer

model, tokenizer = load_model()

st.title("📚 Offline Doubt Solver Bot")
st.write("Ask any academic question, and I'll explain it step by step!")

# User input
user_question = st.text_area("Enter your academic question:")

def generate_response(question):
    inputs = tokenizer(question, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_length=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if st.button("Solve"):
    if not user_question.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Thinking... 🤔"):
            answer = generate_response(user_question)
        st.subheader("📖 Explanation")
        st.write(answer)
