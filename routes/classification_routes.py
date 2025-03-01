from flask import Blueprint, request, jsonify
from models.classification import classify_document
import os
from config import Config

classification_bp = Blueprint('classification', __name__)

@classification_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and file.filename.split('.')[-1].lower() in Config.ALLOWED_EXTENSIONS:
        file_path = os.path.join(Config.UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        result = classify_document(file_path)
        return jsonify(result)
    else:
        return jsonify({"error": "Invalid file type"}), 400
