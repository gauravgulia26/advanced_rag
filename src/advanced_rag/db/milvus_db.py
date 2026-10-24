from functools import lru_cache

from langchain_milvus import Milvus

from ..app.embedding_factory.openai_embedding import OPENAI_EMBEDDING
from ..config.credentials import MILVUS_ENDPOINT, MILVUS_TOKEN


@lru_cache(maxsize=1)
def get_vector_store() -> Milvus:

    return Milvus(
        embedding_function=OPENAI_EMBEDDING,
        collection_name="ethanol_collection_openai",
        collection_description="collection from open ai endpoint",
        connection_args={"uri": MILVUS_ENDPOINT, "token": MILVUS_TOKEN},
        index_params={"index_type": "FLAT", "metric_type": "L2"},
    )
