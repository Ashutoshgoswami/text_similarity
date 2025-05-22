from fastapi import FastAPI
from pydantic import BaseModel
from app.model import compute_similarity
import uvicorn

app = FastAPI()

class TextPair(BaseModel):
    text1: str
    text2: str

@app.post("/")
def get_similarity_score(payload: TextPair):
    score = compute_similarity(payload.text1, payload.text2)
    return {"similarity score": score}

if __name__ == '__main__':
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
