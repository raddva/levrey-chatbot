import streamlit as st
from chatbot import chat_with_bot

st.set_page_config(page_title="Talk with Levrey", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.chat-container {
    display: flex;
    margin-bottom: 10px;
}
.chat-bubble {
    padding: 10px 14px;
    border-radius: 12px;
    max-width: 70%;
    font-size: 16px;
    line-height: 1.4;
}
.assistant {
    background-color: #f1f1f1;
    color: #000;
    align-self: flex-start;
}
.user {
    background-color: #4a90e2;
    color: white;
    margin-left: auto;
    align-self: flex-end;
}
.info-label {
    color: #888;
    font-size: 13px;
    margin-top: 4px;
}

/* Typing dots animation inside spinner */
.stSpinner > div > div {
    display: flex;
    align-items: center;
    gap: 4px;
}
.stSpinner > div > div:after {
    content: '';
    display: inline-block;
    width: 6px;
    height: 6px;
    background-color: #555;
    border-radius: 50%;
    animation: blink 1.2s infinite both;
    box-shadow: 10px 0 #555, 20px 0 #555;
}
@keyframes blink {
    0%   { box-shadow: 10px 0 #555, 20px 0 #555; }
    33%  { box-shadow: 10px 0 transparent, 20px 0 #555; }
    66%  { box-shadow: 10px 0 transparent, 20px 0 transparent; }
    100% { box-shadow: 10px 0 #555, 20px 0 #555; }
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Levrey - Your Chat Buddy")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "A helpful and intelligent assistant."}
    ]

for msg in st.session_state.chat_history:
    if msg["role"] in {"user", "assistant"}:
        alignment = "user" if msg["role"] == "user" else "assistant"
        st.markdown(
            f'<div class="chat-container"><div class="chat-bubble {alignment}">{msg["content"]}</div></div>',
            unsafe_allow_html=True
        )

st.markdown('<div class="info-label">💡 Your conversation is not saved. Refreshing will remove it.</div>', unsafe_allow_html=True)
user_prompt = st.chat_input("Write anything...")

if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    st.markdown(
        f'<div class="chat-container"><div class="chat-bubble user">{user_prompt}</div></div>',
        unsafe_allow_html=True
    )

    with st.spinner(""):
        response = chat_with_bot(user_prompt)

    st.markdown(
        f'<div class="chat-container"><div class="chat-bubble assistant">{response}</div></div>',
        unsafe_allow_html=True
    )
    st.session_state.chat_history.append({"role": "assistant", "content": response})
