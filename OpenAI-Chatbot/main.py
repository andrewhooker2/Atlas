# This is a sample Python script to act as a chatbot with openAI
import openai
import header
from chat import chat_with_openai, grab_ai_message
from embedding import gen_embedding
import qdrant

# Initialize conversation history
conversation_history = []


def search():
    while True:
        search_text = input("Enter what you want to search for: ")
        embedding = gen_embedding(search_text)
        search_result = qdrant.search_similar_vectors(embedding)
        print(search_result)

        r = input("Search Again [ yes | no ]:")

        if r.lower() == "no":
            break


def conversation():
    while True:

        counter = 0
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        # Talking to OpenAI
        print("...")
        response = chat_with_openai(user_input, conversation_history)

        ai_message = grab_ai_message(response, conversation_history)
        print(f"AI: {ai_message}")

        # Creating Embedding
        embedding = gen_embedding(ai_message)

        # Creating Point
        # qdrant.create_point(embedding, counter, response.openai_id)
        qdrant.temp_create_point(embedding, counter, response.openai_id, ai_message)
        counter = counter + 1


def load_chat():
    combined_questions = [
        "Can you explain the theory of general relativity in simple terms?",
        "Could you simplify the concept of quantum mechanics for me?",
        "How would you describe the process of evolution to a child?",
        "Can you break down how a computer works for someone who doesn't know about technology?",
        "What's the easiest way to understand the stock market?",
        "What are some quick and healthy breakfast ideas?",
        "Can you list the winners of the last five Super Bowls?",
        "How do you change a car tire?",
        "What are the steps to publish a book independently?",
        "Could you provide tips for taking professional-quality photographs?"
    ]
    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})
    counter = 0

    print("Sending questions to OPENAI... Please be patient this can take time...")
    try:
        for question in combined_questions:
            user_input = question

            # Talking to OpenAI
            print("Sending questions to OPENAI... Please be patient this can take time...")
            response = chat_with_openai(user_input, conversation_history)
            ai_message = grab_ai_message(response, conversation_history)

            # Creating Embedding
            embedding = gen_embedding(ai_message)

            # Creating Point
            # qdrant.create_point(embedding, counter, response.openai_id)
            qdrant.temp_create_point(embedding, counter, response.openai_id, ai_message)
            counter = counter + 1
            print(f"[{counter}] Completed")

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        print("There might have been an issue talking to OpenAI please try again.")

    print("Messages are now loaded in Qdrant!")


def main():
    # Creating Collection in qdrant
    qdrant.create_collection()

    # Printing Header feel free to remove!
    header.header_print()

    # Prompt to ask the user for their choice
    question_prompt = """
    Would you like to:
    1. Load a pre-existing set of questions
    2. Fill in your own questions

    Please enter the number corresponding to your choice: """

    # Display the prompt and get the user's response
    user_choice = input(question_prompt)

    print("\n============================================================================\n")
    # Process the user's response
    if user_choice == "1":
        # Code to load the pre-existing question set
        load_chat()
        print("Loading Complete...")
        pass
    elif user_choice == "2":
        # Code to allow the user to fill in their own questions
        conversation()
        pass
    else:
        print("Invalid choice. Please enter 1 or 2.")

    search()


# Run the main function
if __name__ == '__main__':
    main()
