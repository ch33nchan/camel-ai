# memory.py
class Memory:
    def __init__(self):
        self.context = []

    def get_context(self):
        return " ".join(self.context[-5:])  # Return last 5 exchanges as context

    def update_context(self, user_input, agent_response):
        self.context.append(user_input)
        self.context.append(agent_response)

    def clear_context(self):
        self.context = []
