from langchain_core.documents import Document
from rich.progress import track

from ..db.milvus_db import get_vector_store
from .splitter import split_documents


def ingest_documents(
    documents: list[Document],
    batch_size: int = 100,
) -> int:
    if not documents:
        return 0

    chunks = split_documents(documents)
    vector_store = get_vector_store()

    for start in track(
        range(0, len(chunks), batch_size),
        description="Ingesting document batches...",
    ):
        batch = chunks[start : start + batch_size]
        vector_store.add_documents(batch)

    return len(chunks)
