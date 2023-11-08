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
