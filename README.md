# OpenAI Chatbot

This Python script serves as an interface for interacting with the OpenAI API to create a conversational chatbot. It allows for maintaining a conversation history and dynamically generates responses using OpenAI's language models. Feel free to steal this code!

## Features

- Loads configuration from environment variables.
- Manages conversation state to maintain context across exchanges.
- Uses OpenAI's powerful language models for generating responses.
- Interactive chat loop allowing real-time conversation.
- Expand on this and use it as you please this is just a starting point for others.

## Prerequisites

- Python 3.x
- `openai` library
- `python-dotenv` library for loading environment variables

## Installation
It is suggested that you use a virtual enviroment for this.
If you dont know how to make one you can use the following command.
This command will make your virtual enviroment and start it with source.

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required dependencies with pip:
There is a requirements.txt to make this a bit easier for new people.
Just make sure you see (venv) before running this command. 

```bash
pip install -r requirements.txt
```

## Configuration
Make sure to replace the filler text in the .env with your actual OpenAI API key and set the other environment variables according to your requirements.
