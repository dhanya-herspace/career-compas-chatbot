import streamlit as st
import requests

st.set_page_config(page_title="Career Compass", page_icon="🧭")
st.title("🧭 Career Compass Chatbot")
st.caption("Ask career-related questions and explore your options.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for chat_message in st.session_state.messages:
    with st.chat_message(chat_message["role"]):
        st.write(chat_message["content"])

user_message = st.chat_input("Type your career question here...")

if user_message:
        {"role": "user", "content": user_message}
    )

    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": user_message},
                timeout=10
            )
            response.raise_for_status()
            reply = response.json()["bot_reply"]
            st.write(reply)

            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )
        except requests.RequestException:
            error_message = (
                "I can’t connect to the backend. Make sure FastAPI is running on port 8000."
            )
            st.error(error_message)
            st.session_state.messages.append(
                {"role": "assistant", "content": error_message}
            )