import os

from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.environ["GROQ_KEY"]
MILVUS_ENDPOINT = os.environ["MILVUS_ENDPOINT"]
MILVUS_TOKEN = os.environ["MILVUS_TOKEN"]
MILVUS_USER = os.environ["MILVUS_USER"]
MILVUS_PASSWORD = os.environ["MILVUS_PASSWORD"]