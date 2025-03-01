import os
import json
import torch
from transformers import pipeline
from utils.ocr_utils import extract_text
from config import Config

# Load NLP model for classification
classifier = pipeline("zero-shot-classification", model=Config.MODEL_NAME)

# Define categories for classification
CATEGORIES = ["medical", "financial", "legal", "education", "general"]

def classify_document(file_path):
    """Extracts text and classifies the document into predefined categories."""
    text = extract_text(file_path)
    if not text:
        return {"error": "Failed to extract text"}
    
    result = classifier(text, CATEGORIES)
    top_category = result["labels"][0]  # Get highest confidence category
    
    # Move file to categorized folder
    categorized_dir = os.path.join(Config.PROCESSED_FOLDER, top_category)
    os.makedirs(categorized_dir, exist_ok=True)
    new_path = os.path.join(categorized_dir, os.path.basename(file_path))
    os.rename(file_path, new_path)
    
    return {"category": top_category, "file_path": new_path}
