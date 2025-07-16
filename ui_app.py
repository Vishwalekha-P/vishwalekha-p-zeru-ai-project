import streamlit as st
from chatbot import get_bot_response

st.title("Zeru AI Assistant (Offline Demo)")

user_input = st.text_input("You:")
if user_input:
    response = get_bot_response(user_input)
    st.write("Bot:", response)