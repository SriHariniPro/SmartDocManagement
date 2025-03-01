from utils.ocr_utils import extract_text
from utils.llm_utils import classify_text

def extract_and_classify(file_path):
    """Extracts text from a document and classifies it into a category."""
    text = extract_text(file_path)
    
    if not text:
        return {"error": "Text extraction failed"}
    
    category = classify_text(text)
    return {"category": category, "text": text}
