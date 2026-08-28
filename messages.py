from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
st.header("HI")
from dotenv import load_dotenv

load_dotenv()
# api_key=os.getenv("GOOGLE_API_KEY")
model=ChatGoogleGenerativeAI(
    model='gemini-3.6-flash',
    google_api_key=os.getenv("GOOGLE_API_KEY"))

messages=[
    SystemMessage(content='You are a Helpful assistant'),
    HumanMessage(content='tell me about langchain')
]

result =model.invoke(messages)

messages.append(AIMessage(content=result.text))

st.text(result)
