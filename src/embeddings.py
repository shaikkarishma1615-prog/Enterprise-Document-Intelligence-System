from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, chunks):

        texts = [doc.page_content for doc in chunks]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings