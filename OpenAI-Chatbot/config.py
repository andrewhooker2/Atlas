import os
import openai
from dotenv import load_dotenv

# Accessing env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Chat
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = os.getenv("API_VERSION")

# Text Embedding
deployment_name = os.getenv("DEPLOYMENT_NAME")
chat_model = os.getenv("OPENAI_MODEL")
text_embedding_model = os.getenv("TEXT_EMBEDDING_MODEL")
openai_vector_dimension = 1536  # This changes depending on model

# Qdrant
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("CLUSTER_API_KEY")
qdrant_collection = os.getenv("QDRANT_COLLECTION_NAME")
