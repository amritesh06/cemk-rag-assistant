import os
import json
from functools import lru_cache

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

from langchain_core.documents import Document

from kb_loader import load_kb_documents, iter_kb_records
from bm25 import BM25


working_dir = os.path.dirname(os.path.abspath(__file__))

# Knowledge base (permanent) and user-uploaded PDF (temporary) live in separate stores
KB_DIR = os.environ.get("CEMK_KB_DIR", os.path.join(working_dir, "cemk-rag-data"))
KB_PERSIST_DIR = os.path.join(working_dir, "kb_vectorstore")
KB_COLLECTION = "cemk_kb"
UPLOAD_PERSIST_DIR = os.path.join(working_dir, "doc_vectorstore")
UPLOAD_COLLECTION = "uploaded_doc"


def _load_api_key():
    key = os.environ.get("GROQ_API_KEY")
    if key:
        return key
    with open(os.path.join(working_dir, "config.json")) as f:
        return json.load(f)["GROQ_API_KEY"]


os.environ["GROQ_API_KEY"] = _load_api_key()


@lru_cache(maxsize=1)
def get_embedding():
    return HuggingFaceEmbeddings()


# llama-3.3-70b-versatile was shut down by Groq on 16 Aug 2026.
# Override with the GROQ_MODEL env var (e.g. "qwen/qwen3.6-27b") if you want another model.
GROQ_MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")


@lru_cache(maxsize=1)
def get_llm():
    return ChatGroq(model=GROQ_MODEL, temperature=0)


def _store(persist_dir, collection):
    return Chroma(
        collection_name=collection,
        persist_directory=persist_dir,
        embedding_function=get_embedding(),
    )


# --------------------------------------------------------------------------
# Knowledge base
# --------------------------------------------------------------------------
def kb_is_ready():
    try:
        return _store(KB_PERSIST_DIR, KB_COLLECTION)._collection.count() > 0
    except Exception:
        return False


def build_kb_store(kb_dir=None):
    """(Re)build the knowledge-base vector store. Returns number of chunks."""
    docs = load_kb_documents(kb_dir or KB_DIR)

    db = _store(KB_PERSIST_DIR, KB_COLLECTION)
    db.delete_collection()                      # start clean so re-running never duplicates
    db = _store(KB_PERSIST_DIR, KB_COLLECTION)

    batch = 100
    for i in range(0, len(docs), batch):
        db.add_documents(docs[i:i + batch])
    return len(docs)


# --------------------------------------------------------------------------
# Optional: a PDF the user uploads in the app
# --------------------------------------------------------------------------
def process_docoment_to_chroma_db(file_path):
    documents = PyPDFLoader(file_path).load()
    if not any(d.page_content.strip() for d in documents):
        raise ValueError(
            "No text could be extracted from this PDF (it may be a scanned/image-only PDF)."
        )

    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    texts = splitter.split_documents(documents)

    _store(UPLOAD_PERSIST_DIR, UPLOAD_COLLECTION).delete_collection()
    Chroma.from_documents(
        documents=texts,
        embedding=get_embedding(),
        collection_name=UPLOAD_COLLECTION,
        persist_directory=UPLOAD_PERSIST_DIR,
    )
    return 0


# --------------------------------------------------------------------------
# Retrieval: vector search + keyword (BM25) search, merged with rank fusion
# --------------------------------------------------------------------------
@lru_cache(maxsize=1)
def _keyword_index():
    """In-memory BM25 index over the same chunks (cheap: no embeddings needed)."""
    if not os.path.isdir(KB_DIR):
        return None
    docs = [Document(page_content=t, metadata=m) for t, m in iter_kb_records(KB_DIR)]
    if not docs:
        return None
    return BM25([d.page_content for d in docs]), docs


def retrieve(question, include_upload=False, k_final=8, k_each=12):
    """Return the best chunks for the question (list of Documents)."""
    ranked_lists = []

    # 1) semantic / vector search
    dense = _store(KB_PERSIST_DIR, KB_COLLECTION).similarity_search(question, k=k_each)
    ranked_lists.append(dense)

    # 2) keyword search (catches exact names, numbers, abbreviations like HOD / NIRF)
    kw = _keyword_index()
    if kw is not None:
        bm, docs = kw
        ranked_lists.append([docs[i] for i in bm.top(question, k=k_each)])

    # Reciprocal-rank fusion
    scores, by_key = {}, {}
    for lst in ranked_lists:
        for rank, d in enumerate(lst):
            key = d.page_content
            by_key[key] = d
            scores[key] = scores.get(key, 0.0) + 1.0 / (60 + rank)
    best = sorted(scores, key=scores.get, reverse=True)[:k_final]
    results = [by_key[k] for k in best]

    if include_upload:
        up = _store(UPLOAD_PERSIST_DIR, UPLOAD_COLLECTION)
        if up._collection.count() > 0:
            results += up.similarity_search(question, k=4)
    return results


# --------------------------------------------------------------------------
# Question answering
# --------------------------------------------------------------------------
PROMPT = """You are the helpful assistant for the College of Engineering & Management, Kolaghat (CEMK).
Answer the question using the context below. The context is a set of excerpts from the college knowledge base.

Rules:
- Read ALL the excerpts and combine information from several of them when needed. Tables are given in markdown.
- The same thing can be worded differently (for example, the head of the institute is the "Director"; HOD = Head of Department; "intake" = number of seats). Use such equivalents.
- Give the specific details you find (names, numbers, dates, emails, phone numbers, URLs) exactly as written.
- Only if the excerpts really contain nothing relevant, say that this information is not available in the knowledge base. If they contain part of the answer, give that part and say what is missing.

Context:
{context}

Question: {question}

Answer:"""


def answer_question(user_question, include_upload=False):
    """Returns (answer_text, sources, retrieved_docs)."""
    docs = retrieve(user_question, include_upload=include_upload)

    blocks = []
    for i, d in enumerate(docs, 1):
        url = d.metadata.get("source_url") or d.metadata.get("source", "")
        blocks.append(f"[Excerpt {i}]\n{d.page_content}\n(source: {url})")
    context = "\n\n".join(blocks)

    msg = get_llm().invoke(PROMPT.format(context=context, question=user_question))
    answer = (msg.content or "").strip() or "The model returned an empty answer. Please try again."

    seen, sources = set(), []
    for d in docs:
        key = (d.metadata.get("section", ""), d.metadata.get("source_url", ""))
        if key not in seen:
            seen.add(key)
            sources.append(
                {"section": key[0] or d.metadata.get("source", "uploaded PDF"), "url": key[1]}
            )
    return answer, sources, docs
