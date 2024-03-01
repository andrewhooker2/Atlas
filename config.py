import os
import openai

# Chat
openai.api_key = os.environ["OPENAI_API_KEY"]
chat_model = os.environ["OPENAI_MODEL"]

# Text Embedding
text_embedding_model = os.environ["TEXT_EMBEDDING_MODEL"]
openai_vector_dimension = 1536

# Qdrant
qdrant_url = os.environ["QDRANT_URL"]
qdrant_api_key = os.environ["QDRANT_CLUSTER_KEY"]
qdrant_collection = "TEST"
