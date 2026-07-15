from sentence_transformers import SentenceTransformer

# Load model once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    """
    Generate an embedding vector for the input text.
    """
    embedding = model.encode(text)

    return embedding.tolist()