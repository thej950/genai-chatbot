from app.services.embeddings import generate_embedding

text = "Amazon Bedrock provides foundation models."

embedding = generate_embedding(text)

print(len(embedding))
print(embedding[:10])  # Print first 10 values