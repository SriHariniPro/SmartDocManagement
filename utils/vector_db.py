import faiss
import numpy as np

class VectorDB:
    def __init__(self, embedding_dim=768):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = []  # Stores document metadata
    
    def add_document(self, doc_id, embedding):
        """Adds a document embedding to the FAISS index."""
        self.index.add(np.array([embedding], dtype=np.float32))
        self.documents.append(doc_id)
    
    def search(self, query_embedding, top_k=5):
        """Searches for the most relevant documents."""
        distances, indices = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        results = [(self.documents[idx], distances[0][i]) for i, idx in enumerate(indices[0]) if idx < len(self.documents)]
        return results