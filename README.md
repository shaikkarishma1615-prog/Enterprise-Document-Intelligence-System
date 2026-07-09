# IntelliDocs AI - Enterprise Document Intelligence System

An AI-powered Enterprise Document Intelligence platform that enables users to upload PDF documents, ask natural language questions, generate summaries, and retrieve accurate answers using Retrieval-Augmented Generation (RAG).

---

## Features

- 📂 Upload PDF documents through the web interface
- ✂️ Automatic document chunking
- 🧠 Generate embeddings using Sentence Transformers
- 🗄️ Persistent vector storage using ChromaDB
- 🔍 Semantic document retrieval
- 🤖 AI-powered answers using Google Gemini
- 📚 Source citations for transparency
- 💬 ChatGPT-style conversational interface
- 📊 Dashboard displaying indexed documents and chunks
- ⚡ Built with a modular and scalable architecture

---

## 🏗️ System Architecture

```text
                   PDF Documents
                         │
                         ▼
                Document Loader
                         │
                         ▼
                  Text Chunking
                         │
                         ▼
             Sentence Transformers
                    (Embeddings)
                         │
                         ▼
                  ChromaDB Database
                         │
                         ▼
                Semantic Retriever
                         │
                         ▼
                  Google Gemini
                         │
                         ▼
             Streamlit Web Interface
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| LLM | Google Gemini |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers |
| Frontend | Streamlit |
| Document Processing | PyPDF |
| Environment | Python Virtual Environment |

---

## 📂 Project Structure

```text
Enterprise-Document-Intelligence-System/
│
├── data/
├── screenshots/
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   ├── llm.py
│   ├── document_processor.py
│   └── config.py
│
├── streamlit_app.py
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shaikkarishma1615-prog/Enterprise-Document-Intelligence-System.git
```

Go to the project directory:

```bash
cd Enterprise-Document-Intelligence-System
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## 📸 Application Screenshots

### Home Page

Add:

```
screenshots/home.png
```

---

### Upload PDF

Add:

```
screenshots/upload.png
```

---

### Chat Interface

Add:

```
screenshots/chat.png
```

---

## 🎯 Future Improvements

- Multi-PDF support
- FAISS and Pinecone integration
- User authentication
- Docker deployment
- REST API using FastAPI
- Cloud deployment
- RAGAS evaluation
- Conversation memory

---

## 📚 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Semantic Search
- Vector Databases
- Prompt Engineering
- Streamlit Development
- Python Programming
- AI Application Development

---

## 👩‍💻 Author

**Shaik Karishma**

Computer Science and Data Science

GitHub: https://github.com/shaikkarishma1615-prog

LinkedIn: https://linkedin.com/in/www.linkedin.com/in/shaik-karishma-556178354