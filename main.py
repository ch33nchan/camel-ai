# main.py
from agent import MultiTaskAgent
from reinforcement import train_agent

if __name__ == "__main__":
    agent = MultiTaskAgent(api_key="your_camel_ai_api_key")

    # Sample conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = agent.handle_conversation(user_input)
        print("Agent:", response)

    # Train agent based on feedback
    train_agent()
