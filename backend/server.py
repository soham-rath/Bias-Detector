import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
from fastapi.middleware.cors import CORSMiddleware

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_NAME)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class TextInput(BaseModel):
    text: str

def analyze_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    confidence, pred_class = torch.max(probs, dim=1)
    label_map = {0: "Negative", 1: "Positive"}
    return {"label": label_map[pred_class.item()], "confidence": float(confidence.item())}

@app.post("/analyze")
async def analyze(input: TextInput):
    return analyze_text(input.text)