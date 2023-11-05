# This is a sample Python script to act as a chatbot with openAI
import os
import openai
import header
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = os.getenv("API_VERSION")

deployment_name = os.getenv("DEPLOYMENT_NAME")
model = os.getenv("OPENAI_MODEL")

# Initialize conversation history
conversation_history = []


def chat_with_openai(user_input):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation_history
    )

    # Extract the assistant's message from the response and add it to the conversation history
    print("Chat ID: ", response.openai_id)
    ai_message = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": ai_message})

    return ai_message


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
            ai_response = chat_with_openai(user_input)
            print(f"AI: {ai_response}")
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")


# Run the main function
if __name__ == '__main__':
    main()
