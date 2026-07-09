from src.retriever import Retriever
from src.llm import GeminiLLM


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.llm = GeminiLLM()

    def ask(self, question, history=""):

        results = self.retriever.search(question)

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        context = "\n\n".join(documents)

        answer = self.llm.generate_answer(
            question,
            context,
            history
        )

        return answer, documents, metadata

    def summarize(self):

        results = self.retriever.collection.get()

        context = "\n\n".join(results["documents"])

        return self.llm.summarize_document(context)

    def suggested_questions(self):

        results = self.retriever.collection.get()

        context = "\n\n".join(results["documents"])

        return self.llm.generate_questions(context)