from flask import Flask, request, jsonify
from routes.classification_routes import classification_bp
from routes.extraction_routes import extraction_bp
from routes.search_routes import search_bp
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(classification_bp, url_prefix='/classify')
app.register_blueprint(extraction_bp, url_prefix='/extract')
app.register_blueprint(search_bp, url_prefix='/search')

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return jsonify({"message": "AI Document Management System API is running"})

if __name__ == '__main__':
    app.run(debug=True)
