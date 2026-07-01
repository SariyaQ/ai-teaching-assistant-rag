from pdf_reader import read_pdf
from chunker import chunk_text
from embedding_client import create_embeddings

text = read_pdf("data/17_Efruz_Qurbanova_Seriye_Qasimova_duzelish_final.pdf")

chunks = chunk_text(text, chunk_size=1000)

embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Length of first embedding:", len(embeddings[0]))
