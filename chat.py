import openai
import requests
import config


def grab_ai_message(response, conversation_history):

    ai_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": ai_message})

    return ai_message


def chat_with_openai(user_input, conversation_history):

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Call the OpenAI API amd send conversation history
    try:
        response = openai.chat.completions.create(
            model=config.chat_model,
            messages=conversation_history
        )
        return response
    except requests.Timeout:
        print("Open AI did not respond...")
        return None
    except Exception as e:
        print("OpenAI Error: ", e)
