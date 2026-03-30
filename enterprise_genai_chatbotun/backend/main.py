
from fastapi import FastAPI
from pydantic import BaseModel
from services.rag_pipeline import generate_response

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    response = generate_response(query.question)
    return {"response": response}
