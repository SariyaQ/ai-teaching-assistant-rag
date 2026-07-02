from pdf_reader import read_pdf
from chunker import chunk_text
from embedding_client import create_embeddings
from rag_answer import generate_answer

text = read_pdf("data/17_Efruz_Qurbanova_Seriye_Qasimova_duzelish_final.pdf")

chunks = chunk_text(text, chunk_size=1000)
chunk_embeddings = create_embeddings(chunks)

question = "What is the main objective of this paper?"

answer = generate_answer(question, chunks, chunk_embeddings)

print(answer)
