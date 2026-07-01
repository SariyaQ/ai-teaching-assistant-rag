import math


def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot_product / (norm1 * norm2)


def retrieve_top_chunks(question_embedding, chunks, chunk_embeddings, top_k=3):
    scores = []

    for chunk, embedding in zip(chunks, chunk_embeddings):
        score = cosine_similarity(question_embedding, embedding)
        scores.append((chunk, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_k]
