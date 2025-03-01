import torch
from transformers import pipeline
from config import Config

# Load NLP model
classifier = pipeline("zero-shot-classification", model=Config.MODEL_NAME)

CATEGORIES = ["medical", "financial", "legal", "education", "general"]

def classify_text(text):
    """Classifies text into predefined categories using NLP."""
    if not text:
        return None
    
    result = classifier(text, CATEGORIES)
    return result["labels"][0]  # Return highest confidence category
