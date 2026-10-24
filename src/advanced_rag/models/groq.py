from langchain_groq import ChatGroq

from ..config.credentials import GROQ_KEY


def get_llm(model_name: str = "openai/gpt-oss-20b") -> ChatGroq:
    return ChatGroq(api_key=GROQ_KEY, model=model_name)
