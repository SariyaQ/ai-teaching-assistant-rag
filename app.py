import os
import streamlit as st

from src.rag_pipeline import prepare_document
from src.rag_answer import generate_answer

st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Teaching Assistant")
st.caption("Ask questions based only on your uploaded PDF document.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "chunk_embeddings" not in st.session_state:
    st.session_state.chunk_embeddings = None

if "file_name" not in st.session_state:
    st.session_state.file_name = None

with st.sidebar:
    st.header("📄 Document")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        file_path = os.path.join("uploads", uploaded_file.name)

        if st.session_state.file_name != uploaded_file.name:
            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

            st.session_state.messages = []

            with st.spinner("Preparing document..."):
                chunks, chunk_embeddings = prepare_document(file_path)

            st.session_state.chunks = chunks
            st.session_state.chunk_embeddings = chunk_embeddings
            st.session_state.file_name = uploaded_file.name

            st.success("Document prepared successfully.")

        st.markdown("### Status")
        st.success("🟢 Ready")

        st.markdown("### File")
        st.write(st.session_state.file_name)

        st.markdown("### Chunks")
        st.write(len(st.session_state.chunks))

        if st.button("Clear chat"):
            st.session_state.messages = []
            st.rerun()
    else:
        st.warning("Please upload a PDF.")

st.markdown("## 💬 Chat")

if st.session_state.chunks is None:
    st.info("Upload a PDF from the sidebar to start asking questions.")
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.chat_input("Ask anything about your document...")

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Searching document and generating answer..."):
            answer = generate_answer(
                question,
                st.session_state.chunks,
                st.session_state.chunk_embeddings
            )

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.write(answer)
