from pymilvus import MilvusClient

from advanced_rag.config.credentials import (
    MILVUS_ENDPOINT,
    MILVUS_PASSWORD,
    MILVUS_TOKEN,
    MILVUS_USER,
)

client = MilvusClient(
    uri=MILVUS_ENDPOINT,
    token=MILVUS_TOKEN,
    user=MILVUS_USER,
    password=MILVUS_PASSWORD,
    timeout=5.0,
)
client.rename_collection(old_name="test_collection", new_name="ethanol_collection")
client.close()
print("done")
