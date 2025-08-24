from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModel
import torch

# Load model & tokenizer with trust_remote_code=True
MODEL_NAME = "nomic-ai/nomic-embed-text-v1.5"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_NAME, trust_remote_code=True)

app = FastAPI()

class EmbedRequest(BaseModel):
    text: str

@app.post("/embed")
def embed(request: EmbedRequest):
    inputs = tokenizer(request.text, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1).squeeze().tolist()
    return {"embedding": embeddings}
