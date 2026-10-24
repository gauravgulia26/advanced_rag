from .hf_embeddings import get_embedding_model as get_hf_embedding_local
from .openai_embeddings import get_openai_embedding

__all__ = ["get_hf_embedding_local", "get_openai_embedding"]
