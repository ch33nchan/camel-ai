# Camel AI-Powered Multi-Tasking Chatbot

This repository contains a multi-tasking AI chatbot built using Camel AI's REST API. The chatbot performs various tasks, including question answering, summarization, translation, and sentiment analysis. It utilizes a memory component to provide contextual responses and dynamically determine the most suitable task for each user input.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to leverage Camel AI's capabilities to create a conversational AI agent capable of handling multiple types of tasks. By providing a structured pipeline, the chatbot can perform diverse tasks based on user input, making it versatile and adaptable.

This chatbot identifies the intended task from the user's input (e.g., summarization, translation) and sends the relevant request to Camel AI via HTTP requests. A contextual memory component stores prior conversations to provide a more natural flow in conversations.

## Features

- **Multi-Tasking**: Supports question answering, summarization, translation, and sentiment analysis.
- **Contextual Memory**: Remembers the conversation history for context-aware responses.
- **Task Identification**: Dynamically detects the user’s intended task based on keywords or phrases.
- **REST API-Based**: Uses direct HTTP requests to communicate with Camel AI’s REST API.

## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/camel-ai-chatbot.git
    cd camel-ai-chatbot
    ```

2. **Install Dependencies**

    - Install the required Python packages:

      ```bash
      pip install -r requirements.txt
      ```

3. **Set Up API Key**

    - Obtain an API key from Camel AI.
    - Create a `.env` file in the root directory of your project and add your API key:

      ```plaintext
      CAMEL_AI_API_KEY=your_api_key_here
      ```

4. **Run the Chatbot**

    Start the chatbot by running the main script:

    ```bash
    python main.py
    ```

## Usage

- Run `main.py` to start the chatbot. The chatbot will prompt you to enter text, identify the task, and return the response based on Camel AI’s analysis.
- Example tasks:
    - **Question Answering**: "What is the capital of France?"
    - **Summarization**: "Summarize the following article: ..."
    - **Translation**: "Translate this to Spanish: Hello!"
    - **Sentiment Analysis**: "Analyze the sentiment of this text: I am feeling great!"

## File Structure

```plaintext
camel-ai-chatbot/
├── agent.py            # Core agent logic for task handling and API communication
├── memory.py           # Contextual memory module for storing conversation history
├── main.py             # Main script to run the chatbot
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (contains API key)
└── examples/           # Sample inputs and outputs
