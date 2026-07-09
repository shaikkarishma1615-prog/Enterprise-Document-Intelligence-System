from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:

    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)

    def load_documents(self):

        loader = PyPDFLoader(str(self.pdf_path))

        return loader.load()