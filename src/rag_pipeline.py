from src.retriever import Retriever
from src.llm import GeminiLLM


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = GeminiLLM()

    def ask(self, question):

        results = self.retriever.search(question)

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        context = "\n\n".join(documents)

        answer = self.llm.generate_answer(question, context)

        return answer, documents, metadata