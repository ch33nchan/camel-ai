# agent.py
import requests
import numpy as np
from memory import Memory

class MultiTaskAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.camel-ai.org"  # Replace with Camel AI's actual API URL
        self.memory = Memory()  # For contextual memory
        self.tasks = ["qa", "summarization", "translation", "sentiment_analysis"]

    def make_request(self, endpoint, payload):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.base_url}/{endpoint}", headers=headers, json=payload)
        if response.status_code == 200:
            return response.json().get("result")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "An error occurred."

    def perform_task(self, task, input_text):
        if task not in self.tasks:
            raise ValueError("Invalid task provided")

        payload = {"text": input_text}

        if task == "qa":
            return self.make_request("question-answering", payload)
        elif task == "summarization":
            return self.make_request("summarize", payload)
        elif task == "translation":
            return self.make_request("translate", payload)
        elif task == "sentiment_analysis":
            return self.make_request("sentiment-analysis", payload)

    def handle_conversation(self, user_input):
        context = self.memory.get_context()  # Retrieve context if needed
        task = self.identify_task(user_input)  # Implement a function to map user input to a task
        response = self.perform_task(task, user_input)
        self.memory.update_context(user_input, response)  # Update context after response
        return response

    def identify_task(self, user_input):
        # Simple logic to identify task based on keywords (could be enhanced with NLP)
        if "translate" in user_input:
            return "translation"
        elif "summarize" in user_input:
            return "summarization"
        elif "sentiment" in user_input:
            return "sentiment_analysis"
        else:
            return "qa"
