from flask import Blueprint, request, jsonify
from search import search_by_content, search_by_tag

search_bp = Blueprint("search", __name__)

@search_bp.route("/content", methods=["GET"])
def search_content():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    results = search_by_content(query)
    return jsonify({"results": results})

@search_bp.route("/tag", methods=["GET"])
def search_tag():
    tag = request.args.get("tag")
    if not tag:
        return jsonify({"error": "Tag parameter is required"}), 400
    
    results = search_by_tag(tag)
    return jsonify({"results": results})
