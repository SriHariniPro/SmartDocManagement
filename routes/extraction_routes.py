from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from extraction import extract_and_classify
from storage import save_file
from config import Config

extraction_bp = Blueprint("extraction", __name__)

@extraction_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(file_path)
    
    result = extract_and_classify(file_path)
    if "error" in result:
        return jsonify(result), 500
    
    category = result["category"]
    new_file_path = save_file(file, category)
    
    return jsonify({
        "category": category,
        "file_path": new_file_path,
        "text": result["text"]
    })
