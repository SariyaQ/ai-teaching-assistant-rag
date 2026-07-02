from openai import OpenAI
from dotenv import load_dotenv

from src. embedding_client import create_embeddings
from src. retriever import retrieve_top_chunks

load_dotenv()

client = OpenAI()


def generate_answer(question, chunks, chunk_embeddings, top_k=3, threshold=0.15):
    question_embedding = create_embeddings([question])[0]

    results = retrieve_top_chunks(
        question_embedding,
        chunks,
        chunk_embeddings,
        top_k=top_k
    )

    best_score = results[0][1]

    if best_score < threshold:
        return "I couldn't find relevant information in the provided document."

    context = "\n\n".join([chunk for chunk, score in results])

    prompt = f"""
You are a helpful teaching assistant.

Answer the question using ONLY the context below.
If the answer is not in the context, say:
"I couldn't find relevant information in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
