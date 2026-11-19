"""Build the knowledge-base vector store once:   python ingest_kb.py"""
from rag_utility import build_kb_store, KB_DIR

if __name__ == "__main__":
    print(f"Reading knowledge base from: {KB_DIR}")
    n = build_kb_store()
    print(f"Done. Indexed {n} chunks into kb_vectorstore/")
