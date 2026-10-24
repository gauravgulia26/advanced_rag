from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings

from ..utils import load_param


@lru_cache(maxsize=1)
def get_embedding_model() -> HuggingFaceEmbeddings:
    _ = load_param(
        key="embedding",
        param_file="/home/gaurav/Documents/advanced_rag/config/params.yaml",
    )
    return HuggingFaceEmbeddings(
        model_name=_["hf_model"], model_kwargs={"device": "cuda"}
    )
