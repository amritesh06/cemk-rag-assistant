"""See exactly which chunks are retrieved for a question (no LLM call):
       python debug_retrieval.py "Who is the HOD of CSE?"
"""
import sys
from rag_utility import retrieve

q = " ".join(sys.argv[1:]) or "Who is the director of CEMK?"
for i, d in enumerate(retrieve(q), 1):
    print(f"\n===== {i}. {d.metadata.get('section')}  [{d.metadata.get('source_file')}]")
    print(d.page_content[:600])
