from flask import Blueprint, jsonify, request
from services.prompt_service import workload
import os

prompt_bp = Blueprint("prompt", __name__)

@prompt_bp.route("/prompt", methods=["POST"])
def prompt():
    header_auth = request.headers.get("Authorization")
    if not header_auth:
        return jsonify({"error": "Ausente Authorization no Header"}), 401
    data = request.json
    prompt = data.get("prompt")
    resultado = workload(prompt)
    return resultado