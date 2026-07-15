from app.services.embeddings import generate_embedding
from app.services.vector_store import VectorStore

texts = [
    "Python is a programming language.",
    "Amazon Bedrock provides foundation models.",
    "FastAPI builds APIs."
]

embeddings = [
    generate_embedding(t)
    for t in texts
]

dimension = len(embeddings[0])

store = VectorStore(dimension)

for emb, text in zip(embeddings, texts):

    store.add(emb, text)

question = "Which AWS service provides AI models?"

question_embedding = generate_embedding(question)

results = store.search(question_embedding)

print(results)