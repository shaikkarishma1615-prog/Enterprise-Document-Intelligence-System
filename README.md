# IntelliDocs AI – Enterprise Document Intelligence Platform

An AI-powered Enterprise Document Intelligence System that enables users to upload PDF documents, ask questions in natural language, generate summaries, and receive accurate answers with citations using Retrieval-Augmented Generation (RAG).

---

##  Features

-  Upload one or multiple PDF documents
-  AI-powered Question Answering using Google Gemini
-  Semantic Search with ChromaDB
- Retrieval-Augmented Generation (RAG)
- Automatic Document Summarization
-  AI-generated Suggested Questions
- Source Citations with page numbers
- FastAPI REST API
- Interactive Streamlit UI
- Docker Support
- Logging for monitoring and debugging

---

#  Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

#  Run the FastAPI Server

```bash
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

#  Docker

Build the Docker image:

```bash
docker build -t intellidocs-ai .
```

Run the container:

```bash
docker run -p 8501:8501 intellidocs-ai
```

---

#  Screenshots

## Home

![Home](screenshots/home.png)

---

##  Upload Documents

![Upload](screenshots/upload.png)

---

##  Ask Questions

![Ask](screenshots/ask.png)

---

##  AI Summary

![Summary](screenshots/summary.png)

---

##  Suggested Questions

![Questions](screenshots/questions.png)

---


#  Author

**Shaik Karishma**

- GitHub: https://github.com/shaikkarishma1615-prog

