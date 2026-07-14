from fastapi import FastAPI

app = FastAPI(title="GenAI Chatbot")

@app.get("/")
def home():
    return {
        "message": "GenAI Chatbot API is running"
    }