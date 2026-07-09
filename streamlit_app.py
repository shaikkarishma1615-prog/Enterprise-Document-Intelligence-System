import os
import streamlit as st

from src.rag_pipeline import RAGPipeline
from src.document_processor import DocumentProcessor


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="IntelliDocs AI",
    page_icon="🚀",
    layout="wide"
)


# -----------------------------
# Load RAG Pipeline
# -----------------------------
@st.cache_resource
def load_pipeline():
    return RAGPipeline()


rag = load_pipeline()
processor = DocumentProcessor()


# -----------------------------
# Header
# -----------------------------
st.title("🚀 IntelliDocs AI")

st.markdown("""
### Enterprise Document Intelligence Platform

Chat with your uploaded PDF using **Google Gemini + ChromaDB + LangChain**
""")

st.divider()


# -----------------------------
# Dashboard
# -----------------------------
try:
    collection = rag.retriever.collection

    total_chunks = collection.count()

    all_metadata = collection.get()["metadatas"]

    total_docs = len(
        set(
            meta.get("source", "Unknown")
            for meta in all_metadata
        )
    )

except Exception:
    total_docs = 0
    total_chunks = 0


c1, c2, c3, c4 = st.columns(4)

c1.metric("📄 Documents", total_docs)
c2.metric("🧩 Chunks", total_chunks)
c3.metric("🧠 Embeddings", "MiniLM")
c4.metric("🤖 LLM", "Gemini")

st.divider()


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("📂 Document Manager")

    uploaded_files = st.file_uploader(
        "Upload PDF(s)",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if not os.path.exists("data"):
            os.makedirs("data")

        for uploaded_file in uploaded_files:

            save_path = os.path.join("data", uploaded_file.name)

            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        if st.button("🚀 Process Documents"):

            with st.spinner("Generating embeddings..."):

                processor.vector_db.reset()

                docs, chunks = processor.process(save_path)

            st.success(
                f"✅ Indexed {docs} document(s) with {chunks} chunks!"
            )

            st.cache_resource.clear()

            st.rerun()

    st.divider()

    st.header("⚙️ System")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.info(f"""
Documents Indexed: **{total_docs}**

Chunks Stored: **{total_chunks}**
""")


# -----------------------------
# AI Summary
# -----------------------------
st.subheader("📄 AI Document Summary")

if st.button("📄 Generate Summary"):

    with st.spinner("Generating summary..."):

        summary = rag.summarize()

    st.session_state["summary"] = summary


if "summary" in st.session_state:

    st.success(st.session_state["summary"])

st.divider()
st.subheader("💡 Suggested Questions")

if st.button("Generate Questions"):

    with st.spinner("Generating questions..."):

        questions = rag.suggested_questions()

    st.session_state["questions"] = questions


if "questions" in st.session_state:

    for question in st.session_state["questions"]:

        if question.strip():

            st.markdown(f"• {question.strip('- ').strip()}")



# -----------------------------
# Chat Section
# -----------------------------
st.subheader("💬 AI Assistant")

st.caption(
    "Ask questions about your uploaded documents."
)


# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input(
    "Ask a question about your documents..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):
            history = ""
        for msg in st.session_state.messages:
            history += f"{msg['role']}: {msg['content']}\n"

        answer, docs, metadata = rag.ask(
            question,
            history
    )

        st.markdown(answer)

        with st.expander("📄 View Sources"):

            for i, (doc, meta) in enumerate(
                zip(docs, metadata),
                start=1
            ):

                st.markdown(f"### Source {i}")

                st.write(
                    f"**File:** {meta.get('source', 'Unknown')}"
                )

                if "page" in meta:
                    st.write(
                        f"**Page:** {meta['page'] + 1}"
                    )

                st.code(doc)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )