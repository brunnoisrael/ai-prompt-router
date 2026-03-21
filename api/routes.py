from flask import Blueprint, jsonify, request, Response
from services.prompt_service import workload
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import os

# Registra a Blueprint da rota de prompt (POST)
prompt_bp = Blueprint("prompt", __name__)

@prompt_bp.route("/prompt", methods=["POST"])
def prompt():

    # Solicita TOKEN de autorização no header
    header_auth = request.headers.get("Authorization")

    # Verifica se o header_auth (autorização no cabeçalho) foi passado
    if not header_auth:
        return jsonify({"error": "Ausente Authorization no Header"}), 401
    
    data = request.json

    # Solicita "prompt:" no body
    prompt = data.get("prompt")

    # Passa o prompt para o prompt_service orquestrar as chamadas das SLMs e LLMs
    resultado = workload(prompt)
    return resultado

# Registra a Blueprint da rota de metricas do Prometheus
metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)