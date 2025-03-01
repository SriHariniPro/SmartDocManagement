from transformers import pipeline

# Load a small transformer model for efficiency
semantic_analyzer = pipeline("text-classification", model="distilbert-base-uncased")

def analyze_semantics(text):
    """Performs semantic analysis on the extracted text."""
    if not text:
        return {"error": "No text provided"}
    
    analysis = semantic_analyzer(text)
    return {"label": analysis[0]['label'], "score": analysis[0]['score']}
