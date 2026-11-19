import os
import streamlit as st

from rag_utility import (
    process_docoment_to_chroma_db,
    answer_question,
    kb_is_ready,
    build_kb_store,
    KB_DIR,
)

working_dir = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(working_dir, "uploads")
os.makedirs(upload_dir, exist_ok=True)

st.title("CEMK Kolaghat - Knowledge Base Assistant")

# ---- Knowledge base: built automatically the first time ----
if not kb_is_ready():
    if not os.path.isdir(KB_DIR):
        st.error(f"Knowledge-base folder not found: {KB_DIR}\n\n"
                 "Unzip cemk-rag-data.zip next to main.py.")
        st.stop()
    with st.spinner("Building the knowledge base (first run only, may take a few minutes)..."):
        n = build_kb_store()
    st.success(f"Knowledge base ready ({n} chunks).")

with st.sidebar:
    st.header("Knowledge base")
    st.write("Answers come from the CEMK website data.")
    if st.button("Rebuild knowledge base"):
        with st.spinner("Rebuilding..."):
            n = build_kb_store()
        st.success(f"Rebuilt ({n} chunks).")

    st.divider()
    st.header("Optional: add your own PDF")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    use_upload = False
    if uploaded_file is not None:
        file_key = f"{uploaded_file.name}:{uploaded_file.size}"
        if st.session_state.get("processed_file") != file_key:
            save_path = os.path.join(upload_dir, os.path.basename(uploaded_file.name))
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            try:
                with st.spinner("Processing PDF..."):
                    process_docoment_to_chroma_db(save_path)
                st.session_state["processed_file"] = file_key
            except Exception as e:
                st.session_state.pop("processed_file", None)
                st.error(f"Could not process the PDF: {e}")
        if st.session_state.get("processed_file") == file_key:
            st.info("PDF processed successfully")
            use_upload = st.checkbox("Also search my uploaded PDF", value=True)

user_question = st.text_area("Ask a question about CEMK")

if st.button("Answer"):
    if not user_question.strip():
        st.warning("Please type a question.")
    else:
        try:
            with st.spinner("Thinking..."):
                answer, sources, docs = answer_question(user_question, include_upload=use_upload)
            st.markdown("### Answer")
            st.markdown(answer)
            with st.expander("Sources used"):
                for s in sources:
                    st.markdown(f"- {s['section']}" + (f" — {s['url']}" if s["url"] else ""))
            with st.expander("Retrieved text sent to the model (for debugging)"):
                for i, d in enumerate(docs, 1):
                    st.markdown(f"**Excerpt {i}** — {d.metadata.get('section', '')}")
                    st.code(d.page_content, language="markdown")
        except Exception as e:
            st.error(f"Error while answering: {e}")
