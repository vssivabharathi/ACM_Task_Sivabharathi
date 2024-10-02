import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai



load_dotenv()


st.set_page_config(
    page_title="Chat with Gemini 1.5 flash !",
    page_icon=":brain:",  #Icons from favicon
    layout="centered",
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# using tha api
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.5-flash')



def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role



if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# title of the page
st.title(" Gemini 1.5 flash - ChatBot")

#  chat history ....
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field
user_prompt = st.chat_input("Ask Gemini...")
if user_prompt:
    # Add user
    st.chat_message("user").markdown(user_prompt)

    # Sending text
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # output from gemma 1.5
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)


