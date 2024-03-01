import openai


def gen_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    try:
        response = openai.embeddings.create(input=[text], model=model)
        return response.data[0].embedding
    except Exception as e:
        print(f"OpenAI Embedding Error: {e}")

