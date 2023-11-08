import openai
import requests
import config


def chat_with_openai(user_input, conversation_history):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model=config.model,
        messages=conversation_history
    )

    # Extract the assistant's message from the response and add it to the conversation history
    try:
        ai_message = response['choices'][0]['message']['content']
        conversation_history.append({"role": "assistant", "content": ai_message})
    except requests.Timeout:
        ai_message = "Open AI did not respond..."

    return ai_message
