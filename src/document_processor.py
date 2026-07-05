import os

from src.loader import DocumentLoader
from src.chunker import TextChunker
from src.embeddings import EmbeddingGenerator
from src.vector_store import VectorStore


class DocumentProcessor:

    def __init__(self):

        self.chunker = TextChunker()
        self.embedder = EmbeddingGenerator()
        self.vector_db = VectorStore()

    def process(self, data_folder="data"):

        loader = DocumentLoader(data_folder)

        documents = loader.load_documents()

        chunks = self.chunker.split_documents(documents)

        embeddings = self.embedder.generate_embeddings(chunks)

        self.vector_db.add_documents(
            chunks,
            embeddings
        )

        return len(documents), len(chunks)