import streamlit as st
from chatbot import chat_with_bot

st.set_page_config(page_title="OpenRouter Chatbot", page_icon="🤖")

st.title("🤖 OpenRouter Chatbot (GPT 3.5 Turbo)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "A helpful and intelligent assistant."}
    ]

for msg in st.session_state.chat_history:
    if msg["role"] in {"user", "assistant"}:
        with st.chat_message("user" if msg["role"] == "user" else "assistant"):
            st.markdown(msg["content"])

user_prompt = st.chat_input("Type your message...")

if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_with_bot(user_prompt)
            st.markdown(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
