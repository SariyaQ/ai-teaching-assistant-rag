from pdf_reader import read_pdf
from chunker import chunk_text
from embedding_client import create_embeddings


def prepare_document(file_path, chunk_size=1000):
    text = read_pdf(file_path)

    chunks = chunk_text(text, chunk_size=chunk_size)

    chunk_embeddings = create_embeddings(chunks)

    return chunks, chunk_embeddings
