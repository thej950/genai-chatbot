from app.services.embeddings import generate_embedding
from app.services.vector_store import VectorStore
from app.services.retriever import Retriever

texts = [
    "Python is a programming language.",
    "Amazon Bedrock provides foundation models.",
    "FastAPI is a modern web framework."
]

embeddings = [
    generate_embedding(text)
    for text in texts
]

dimension = len(embeddings[0])

store = VectorStore(dimension)

for emb, text in zip(embeddings, texts):

    store.add(emb, text)

retriever = Retriever(store)

results = retriever.retrieve(
    "Which AWS service provides AI models?"
)

print(results)