from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def create_embeddings(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )

    embeddings = []

    for item in response.data:
        embeddings.append(item.embedding)

    return embeddings
