# frontend.py
import streamlit as st
from agent import MultiTaskAgent

# Initialize agent
agent = MultiTaskAgent(api_key="your_camel_ai_api_key")

st.title("Adaptive Conversational Agent")

user_input = st.text_input("Enter your message:")
if user_input:
    response = agent.handle_conversation(user_input)
    st.write("Agent:", response)

    feedback = st.radio("How was the response?", ("Good", "Bad"))
    if feedback:
        st.write(f"Thank you for your feedback: {feedback}")
        # Integrate feedback into RL here by storing it for reinforcement.py
