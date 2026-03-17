from flask import Blueprint, jsonify, request
from services.prompt_service import workload

prompt_bp = Blueprint("prompt", __name__)

@prompt_bp.route("/prompt", methods=["POST"])
def prompt():
    data = request.json
    prompt = data.get("prompt")
    resultado = workload(prompt)
    return resultado