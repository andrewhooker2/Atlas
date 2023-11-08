# This is a sample Python script to act as a chatbot with openAI
import openai
import header
from chat import chat_with_openai as conversation
from embedding import gen_embedding

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

            ai_response = conversation(user_input, conversation_history)
            print(f"AI: {ai_response}")
            print(gen_embedding(ai_response))

        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")


# Run the main function
if __name__ == '__main__':
    main()
