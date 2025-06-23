# app.py
import streamlit as st
import openai

st.set_page_config(page_title="Simple GenAI Chatbot")

st.title("💬 Chatbot with OpenAI")

# Set your OpenAI API key here or use secrets in deployment
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "your-openai-api-key"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
prompt = st.chat_input("Say something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # OpenAI response
    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response["choices"][0]["message"]["content"]
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

