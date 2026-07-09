from src.loader import DocumentLoader
from src.chunker import TextChunker
from src.embeddings import EmbeddingGenerator
from src.vector_store import VectorStore
from src.logger import logger


class DocumentProcessor:

    def __init__(self):

        self.chunker = TextChunker()
        self.embedder = EmbeddingGenerator()
        self.vector_db = VectorStore()

    def process(self, pdf_path):

        logger.info(f"Loading document: {pdf_path}")

        loader = DocumentLoader(pdf_path)

        documents = loader.load_documents()

        logger.info(f"Loaded {len(documents)} pages.")

        chunks = self.chunker.split_documents(documents)

        logger.info(f"Created {len(chunks)} chunks.")

        embeddings = self.embedder.generate_embeddings(chunks)

        logger.info("Embeddings generated successfully.")

        self.vector_db.add_documents(
            chunks,
            embeddings
        )

        logger.info("Embeddings stored in ChromaDB.")

        return len(documents), len(chunks)