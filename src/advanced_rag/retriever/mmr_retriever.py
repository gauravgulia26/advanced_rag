from functools import lru_cache

from langchain_core.vectorstores import VectorStoreRetriever

from ..app import MILVUS_VECTOR_STORE


@lru_cache(maxsize=1)
def get_mmr_retriever(
    k: int = 3, fetch_k: int = 30, lambda_mult: float = 0.5
) -> VectorStoreRetriever:

    return MILVUS_VECTOR_STORE.as_retriever(
        search_type="mmr",
        search_kwargs={"k": k, "fetch_k": fetch_k, "lambda_mult": lambda_mult},
    )
