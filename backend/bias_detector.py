import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_NAME)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_NAME)

model.eval()

def analyze_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    confidence, pred_class = torch.max(probs, dim=1)
    
    label_map = {0: "Negative", 1: "Positive"}
    return label_map[pred_class.item()], confidence.item()

if __name__ == "__main__":
    print("=== Bias / Sentiment Detector ===")
    while True:
        text = input("\nEnter text (or 'quit' to exit): ")
        if text.lower() == "quit":
            break
        label, confidence = analyze_text(text)
        print(f"Prediction: {label} (Confidence: {confidence:.2f})")
