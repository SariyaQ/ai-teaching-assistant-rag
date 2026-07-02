import os
import streamlit as st

from src.rag_pipeline import prepare_document
from src.rag_answer import generate_answer

st.title("AI Teaching Assistant")
st.write("Upload a PDF and ask questions based only on the document.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully.")

    if "chunks" not in st.session_state:
        with st.spinner("Preparing document..."):
            chunks, chunk_embeddings = prepare_document(file_path)

        st.session_state.chunks = chunks
        st.session_state.chunk_embeddings = chunk_embeddings

        st.success("Document is ready. You can ask questions now.")

    question = st.text_input("Ask a question about the document:")

    if st.button("Ask"):
        if question:
            with st.spinner("Generating answer..."):
                answer = generate_answer(
                    question,
                    st.session_state.chunks,
                    st.session_state.chunk_embeddings
                )

            st.subheader("Answer")
            st.write(answer)
        else:
            st.warning("Please enter a question.")
