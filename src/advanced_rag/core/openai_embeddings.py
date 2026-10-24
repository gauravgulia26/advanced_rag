from functools import lru_cache

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

from ..utils import load_param


@lru_cache(maxsize=1)
def get_openai_embedding() -> OpenAIEmbeddings:
    load_dotenv()
    params = load_param(
        key="embedding",
        param_file="/home/gaurav/Documents/advanced_rag/config/params.yaml",
    )
    return OpenAIEmbeddings(model=params["model"], dimensions=params["dimensions"])
