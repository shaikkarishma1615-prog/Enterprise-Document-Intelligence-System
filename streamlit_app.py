import streamlit as st
from src.rag_pipeline import RAGPipeline

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def load_pipeline():
    return RAGPipeline()

rag = load_pipeline()

st.title("🚀 IntelliDocs AI")

st.markdown(
"""
 Document Intelligence Platform """
)

st.divider()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📄 Documents",
        len(set(
            m.get("source", "")
            for m in rag.retriever.collection.get()["metadatas"]
        ))
    )

with col2:
    st.metric(
        "🧩 Chunks",
        rag.retriever.collection.count()
    )

with col3:
    st.metric(
        "🧠 Embeddings",
        "MiniLM"
    )

with col4:
    st.metric(
        "🤖 LLM",
        "Gemini"
    )

st.divider()
from src.document_processor import DocumentProcessor

processor = DocumentProcessor()

with st.sidebar:

    st.header("📂 Document Manager")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        save_path = f"data/{uploaded_file.name}"

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("🚀 Process Document"):

            with st.spinner("Generating embeddings..."):

                docs, chunks = processor.process()

            st.success(
                f"✅ {docs} document(s), {chunks} chunks indexed."
            )

    st.divider()

    st.header("⚙ System")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.caption("Chat with your documents using Retrieval-Augmented Generation (RAG)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# AI Assistant Section
st.subheader("💬 AI Assistant")


# Chat input
question = st.chat_input("Ask a question about your documents...")

if question:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("🔍 Searching documents..."):

            answer, docs, metadata = rag.ask(question)

        st.markdown(answer)

        with st.expander("📄 View Sources"):

            for i, (doc, meta) in enumerate(zip(docs, metadata), start=1):

                st.markdown(f"### Source {i}")

                st.write(
                    f"**File:** {meta.get('source','Unknown')}"
                )

                if "page" in meta:
                    st.write(
                        f"**Page:** {meta['page']+1}"
                    )

                st.code(doc)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )