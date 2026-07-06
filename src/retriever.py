import chromadb
from sentence_transformers import SentenceTransformer


class Retriever:
    def __init__(self):
        # Load the same embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Connect to ChromaDB
        self.client = chromadb.PersistentClient(path="vector_store")

        # Load existing collection
        self.collection = self.client.get_or_create_collection(
            name="enterprise_rag"
        )

    def search(self, query, top_k=2):
        query_embedding = self.model.encode(query).tolist()

        results = self.collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

        return results
