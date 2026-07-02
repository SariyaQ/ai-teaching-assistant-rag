from rag_pipeline import prepare_document

chunks, chunk_embeddings = prepare_document(
    "data/17_Efruz_Qurbanova_Seriye_Qasimova_duzelish_final.pdf"
)

print("Chunks:", len(chunks))
print("Embeddings:", len(chunk_embeddings))
