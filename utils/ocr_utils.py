import pytesseract
import pdfplumber
import docx
import os
from PIL import Image
from config import Config

pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_PATH

def extract_text(file_path):
    """Extracts text from various document formats."""
    ext = file_path.split('.')[-1].lower()
    text = ""
    
    if ext in ['png', 'jpg', 'jpeg']:
        text = pytesseract.image_to_string(Image.open(file_path))
    elif ext == 'pdf':
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif ext == 'docx':
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    
    return text.strip() if text else None
