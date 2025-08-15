import streamlit as st
import asyncio
from agents import Agent, Runner, ModelSettings
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file


# Page layout
st.set_page_config(page_title="GPT-5 Chat Helper", layout="wide")

# Sidebar for instructions & clear history
with st.sidebar:
    st.header("Instructions")
    st.write("Select reasoning effort, type your question, and see how GPT-5 helper responds 😊")
    if st.button("Clear Chat History"):
        st.session_state.messages = []  # Clear the chat
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

st.title("GPT-5 based Reasoning Chat Helper")

# Reasoning effort selector
effort = st.selectbox("Choose reasoning effort:", ["minimal", "low", "medium", "high"])

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    # Record user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    api_key = os.getenv("OPENAI_API_KEY")  # Ensure the OpenAI API key is set
    if not api_key:
        st.error("Please set your OpenAI API key in the .env file.")
    

    # Prepare agent with reasoning
    model_settings = ModelSettings(reasoning={"effort": effort})
    agent = Agent(
        name="Choti GPT-5",
        instructions="Explain simply, like talking to a 10-year-old.",
        model="gpt-5",
        model_settings=model_settings
    )

    # Get response
    result = asyncio.run(Runner.run(agent, input=prompt))
    reply = result.final_output

    # Display and record assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)


