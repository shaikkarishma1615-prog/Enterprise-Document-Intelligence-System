from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:
    def __init__(self, data_folder="data"):
        self.data_folder = Path(data_folder)

    def load_documents(self):
        documents = []

        for file in self.data_folder.glob("*.pdf"):
            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())

        return documents