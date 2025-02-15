from flask import Blueprint, request, jsonify
from app.services import AuthService

bp = Blueprint("auth", __name__)

@bp.route("/validate", methods=["POST"])
def validate_api_key():
    """Endpoint para validar API Key"""
    data = request.json
    api_key = data.get("api_key")

    response, status = AuthService.validate_api_key(api_key)  # 📌 Llamar al servicio
    return jsonify(response), status