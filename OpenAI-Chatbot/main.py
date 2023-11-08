# This is a sample Python script to act as a chatbot with openAI
import os
import openai
import header
from dotenv import load_dotenv
import chat

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = os.getenv("API_VERSION")

deployment_name = os.getenv("DEPLOYMENT_NAME")
model = os.getenv("OPENAI_MODEL")

# Initialize conversation history
conversation_history = []


def main():
    # Printing Header feel free to remove!
    header.header_print()

    # Start the chat with an introduction message from the system
    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})

    # Chat loop
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break

            ai_response = chat.chat_with_openai(user_input, conversation_history)
            print(f"AI: {ai_response}")
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")


# Run the main function
if __name__ == '__main__':
    main()
