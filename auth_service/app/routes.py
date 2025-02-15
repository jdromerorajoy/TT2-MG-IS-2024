from flask import Blueprint, request, jsonify
from app.utils.logger_client import LoggerClient

bp = Blueprint("auth", __name__)

VALID_KEYS = {
    "freemium_key": "freemium",
    "premium_key": "premium"
}

@bp.route("/validate", methods=["POST"])
def validate_api_key():
    """Valida una API Key"""
    data = request.json
    api_key = data.get("api_key")

    if api_key in VALID_KEYS:
        LoggerClient.info("✅ Autenticación exitosa")
        return jsonify({"valid": True}), 200
    else:
        LoggerClient.warning("🚫 Autenticación fallida")
        return jsonify({"error": "Invalid API Key"}), 403