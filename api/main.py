import os
import shutil

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from src.rag_pipeline import RAGPipeline
from src.document_processor import DocumentProcessor
from src.logger import logger

# -----------------------------
# Initialize FastAPI
# -----------------------------
app = FastAPI(
    title="Enterprise Document Intelligence API",
    version="1.0.0"
)

# -----------------------------
# Initialize Components
# -----------------------------
rag = RAGPipeline()
processor = DocumentProcessor()

# -----------------------------
# Request Models
# -----------------------------
class QuestionRequest(BaseModel):
    question: str


# -----------------------------
# Home Endpoint
# -----------------------------
@app.get("/")
def home():
    logger.info("API Home Endpoint Accessed")

    return {
        "message": "Enterprise Document Intelligence API is running!"
    }


# -----------------------------
# Upload PDF
# -----------------------------
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    logger.info(f"Uploading file: {file.filename}")

    os.makedirs("data", exist_ok=True)

    file_path = os.path.join("data", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info("File saved successfully.")

    # Reset existing vector database
    processor.vector_db.reset()

    logger.info("Vector database reset.")

    # Process uploaded documents
    docs, chunks = processor.process(file_path)

    logger.info(
        f"Successfully processed {docs} document(s) into {chunks} chunks."
    )

    return {
        "message": "Document processed successfully",
        "file": file.filename,
        "documents": docs,
        "chunks": chunks
    }


# -----------------------------
# Ask Question
# -----------------------------
@app.post("/ask")
def ask_question(request: QuestionRequest):

    logger.info(f"Question received: {request.question}")

    answer, docs, metadata = rag.ask(request.question)

    logger.info("Answer generated successfully.")

    sources = []
    seen = set()

    for meta in metadata:

        source = {
            "file": meta.get("source", "").replace("data/", ""),
            "page": meta.get("page", 0) + 1
        }

        key = (source["file"], source["page"])

        if key not in seen:
            seen.add(key)
            sources.append(source)

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }


# -----------------------------
# Generate Summary
# -----------------------------
@app.post("/summary")
def generate_summary():

    logger.info("Generating document summary.")

    summary = rag.summarize()

    logger.info("Summary generated successfully.")

    return {
        "summary": summary
    }


# -----------------------------
# Suggested Questions
# -----------------------------
@app.post("/questions")
def generate_questions():

    logger.info("Generating suggested questions.")

    questions = rag.suggested_questions()

    logger.info("Suggested questions generated.")

    return {
        "questions": questions
    }