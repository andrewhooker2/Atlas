# Importing required modules
import openai
import header
from chat import chat_with_openai, grab_ai_message
from embedding import gen_embedding
import qdrant

# Initialize conversation history
conversation_history = []


def search():
    print("[*] Starting up the search module...")
    while True:
        search_text = input("[?] Enter your query: ")
        embedding = gen_embedding(search_text)
        print("[*] Searching the database...")
        print(f"[+] Search Results Found: ")

        search_results = qdrant.search_similar_vectors(embedding)
        for scored_point in search_results:
            print("Score:", scored_point.score)
            print("Message: ")
            print(scored_point.payload['message'])

        r = input("[?] Search again? (yes/no): ")
        if r.lower() == "no":
            break


def conversation():
    print("[*] Starting conversation module...")
    counter = 0
    while True:
        try:
            user_input = input("👤: ")
            if user_input.lower() == "quit":
                break
            print("[*] Communicating with OpenAI...")
            response = chat_with_openai(user_input, conversation_history)
            ai_message = grab_ai_message(response, conversation_history)
            print(f"💻: {ai_message}")
            print("[*] Creating embedding...")
            embedding = gen_embedding(ai_message)

            print("[*] Storing conversation point...")
            qdrant.temp_create_point(embedding, counter, response.openai_id, ai_message)
            counter += 1
        except Exception as e:
            print("OpenAI has raised an Error: ", e)


def load_chat():
    print("[*] Loading chat module...")
    questions = [
        "Can you explain the theory of general relativity in simple terms?",
        "Could you simplify the concept of quantum mechanics for me?",
        "How would you describe the process of evolution to a child?",
        "Can you break down how a computer works for someone who doesn't know about technology?",
        "What's the easiest way to understand the stock market?"
    ]

    print("[*] Initializing system...")
    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})
    counter = 0

    print("[*] Communicating with OpenAI...")
    try:
        for question in questions:
            response = chat_with_openai(question, conversation_history)
            ai_message = grab_ai_message(response, conversation_history)

            embedding = gen_embedding(ai_message)
            qdrant.temp_create_point(embedding, counter, response.openai_id, ai_message)
            counter += 1
            print(f"[+] Question {counter} | {len(questions)}: Completed")
        print("[+] Loading Completed!")

    except openai.error.OpenAIError as e:
        print(f"OpenAI Loading Error: {e}")


def main():
    qdrant.create_collection()
    header.header_print()

    user_choice = input("[?] Enter your choice:\n\n[1] Load pre-existing questions\n[2] Input your own "
                        "questions\n\nChoice: ")
    if user_choice == "1":
        load_chat()
    elif user_choice == "2":
        conversation()
    else:
        print("[-] Invalid choice...")
    search()


if __name__ == '__main__':
    main()
