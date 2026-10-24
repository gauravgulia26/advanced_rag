from langchain_community.document_loaders import PyPDFLoader

from advanced_rag.ingestion.pipeline import ingest_documents


def ingest_pdf(file_path: str) -> int:
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    return ingest_documents(documents)



