from vectordb import VectorDB
from utils.llm_utils import get_text_embedding
from storage import Config
import os

vector_db = VectorDB()

def search_by_content(query, top_k=5):
    """Search for documents based on content similarity."""
    query_embedding = get_text_embedding(query)
    results = vector_db.search(query_embedding, top_k)
    
    return [{"document": doc_id, "score": score} for doc_id, score in results]

def search_by_tag(tag):
    """Retrieve documents based on their classification tag."""
    tag_folder = os.path.join(Config.UPLOAD_FOLDER, tag)
    if not os.path.exists(tag_folder):
        return []
    
    return os.listdir(tag_folder)
