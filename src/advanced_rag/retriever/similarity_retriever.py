from functools import lru_cache

from langchain_core.vectorstores import VectorStoreRetriever

from ..app import MILVUS_VECTOR_STORE


@lru_cache(maxsize=1)
def get_similarity_retriever() -> VectorStoreRetriever:

    return MILVUS_VECTOR_STORE.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5,
        },
    )
