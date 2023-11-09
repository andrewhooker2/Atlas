# This is a sample Python script to act as a chatbot with openAI
import openai
import header
from chat import chat_with_openai, grab_ai_message
from embedding import gen_embedding
import qdrant

# Initialize conversation history
conversation_history = []


def main():
    counter = 1
    qdrant.create_collection()
    # Printing Header feel free to remove!
    header.header_print()

    # Start the chat with an introduction message from the system
    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})

    # Chat loop
    while True:
        try:
            if counter > 1:
                run = input("Continue? ")
            user_input = input("You: ")
            # user_input = "What color is the sky?"
            if user_input.lower() == "quit":
                break

            # Talking to OpenAI
            print("Sending to OPENAI")
            response = chat_with_openai(user_input, conversation_history)
            print("Getting AI MESSAGE")
            ai_message = grab_ai_message(response, conversation_history)
            print(f"AI: {ai_message}")

            # Creating Embedding
            embedding = gen_embedding(ai_message)

            # Creating Point
            # qdrant.create_point(embedding, counter, response.openai_id)
            qdrant.temp_create_point(embedding, counter, response.openai_id, ai_message)
            counter = counter + 1

        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")


# Run the main function
if __name__ == '__main__':
    main()
