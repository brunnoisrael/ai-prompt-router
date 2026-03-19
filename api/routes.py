from flask import Blueprint, jsonify, request
from flask_login import login_required, login_manager
from services.prompt_service import workload
import os

prompt_bp = Blueprint("prompt", __name__)

@prompt_bp.route("/prompt", methods=["POST"])
@login_required
def prompt():
    header_auth = request.headers.get("Authorization")
    data = request.json
    prompt = data.get("prompt")
    resultado = workload(prompt)
    return resultado