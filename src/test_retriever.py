from pdf_reader import read_pdf
from chunker import chunk_text
from embedding_client import create_embeddings
from retriever import retrieve_top_chunks

text = read_pdf("data/17_Efruz_Qurbanova_Seriye_Qasimova_duzelish_final.pdf")

chunks = chunk_text(text, chunk_size=1000)
chunk_embeddings = create_embeddings(chunks)

question = "What is the main objective of this paper?"
question_embedding = create_embeddings([question])[0]

results = retrieve_top_chunks(
    question_embedding,
    chunks,
    chunk_embeddings,
    top_k=3
)

for i, (chunk, score) in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print("Score:", score)
    print(chunk[:700])
