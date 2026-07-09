import chromadb


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="vector_store")

        self.collection = self.client.get_or_create_collection(
            name="enterprise_rag"
        )

    def reset(self):
        try:
            self.client.delete_collection("enterprise_rag")
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            name="enterprise_rag"
        )

    def add_documents(self, chunks, embeddings):

        ids = []
        documents = []
        metadatas = []
        vectors = []

        for i, chunk in enumerate(chunks):

            ids.append(str(i))
            documents.append(chunk.page_content)
            metadatas.append(chunk.metadata)
            vectors.append(embeddings[i].tolist())

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=vectors
        )

    def count(self):
        return self.collection.count()