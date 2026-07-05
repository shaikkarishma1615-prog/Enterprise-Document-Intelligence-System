from src.rag_pipeline import RAGPipeline

print("=" * 60)
print("Enterprise RAG Chatbot")
print("=" * 60)

rag = RAGPipeline()

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer, docs, metadata = rag.ask(question)

    print("\n" + "=" * 60)
    print("Answer")
    print("=" * 60)
    print(answer)

    print("\n" + "=" * 60)
    print("Sources")
    print("=" * 60)

    for i, (doc, meta) in enumerate(zip(docs, metadata), start=1):

        print(f"\nSource {i}")

        print(f"File : {meta.get('source','Unknown')}")

        if "page" in meta:
            print(f"Page : {meta['page']+1}")

        print("\nContent:")
        print(doc)

        print("-" * 60)