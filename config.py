import os

class Config:
    UPLOAD_FOLDER = 'uploads'
    PROCESSED_FOLDER = 'processed'
    VECTOR_DB_PATH = 'vector_db/'
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'png', 'jpg', 'jpeg'}
    
    # OCR Settings
    TESSERACT_PATH = '/usr/bin/tesseract'  # Update path if needed
    
    # NLP Model
    MODEL_NAME = 'distilbert-base-uncased'
    
    # FAISS Settings
    FAISS_INDEX_FILE = os.path.join(VECTOR_DB_PATH, 'index.faiss')
    FAISS_METADATA_FILE = os.path.join(VECTOR_DB_PATH, 'metadata.json')

# Ensure necessary directories exist
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
os.makedirs(Config.PROCESSED_FOLDER, exist_ok=True)
os.makedirs(Config.VECTOR_DB_PATH, exist_ok=True)
