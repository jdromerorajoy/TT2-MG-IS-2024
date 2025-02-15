from flask import Blueprint, request, jsonify
from app.middleware import require_auth, limiter, get_rate_limit
from app.services import PredictionClient
from app.utils.logger_client import LoggerClient

bp = Blueprint("api", __name__)

@bp.route("/predict", methods=["POST"])
@require_auth
@limiter.limit(get_rate_limit)
def predict():
    """Endpoint para obtener predicción desde `prediction_service`"""

    inputs = request.json.get("inputs", [])

    if not inputs:
        LoggerClient.error("⚠️Solicitud sin datos de entrada")
        return jsonify({"error": "No input provided"}), 400

    LoggerClient.info("📡 Enviando datos al modelo...")
    result = PredictionClient.get_prediction(inputs)
    LoggerClient.info(f"🎯 Predicción obtenida: {result}")

    return jsonify(result)