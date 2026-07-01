from pdf_reader import read_pdf
from chunker import chunk_text

text = read_pdf("data/17_Efruz_Qurbanova_Seriye_Qasimova_duzelish_final.pdf")

chunks = chunk_text(text, chunk_size=1000)

print("Number of chunks:", len(chunks))
print("\nFirst chunk:\n")
print(chunks[0])
