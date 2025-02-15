from flask import Blueprint, request, jsonify
from app.middleware import start_request, require_auth, limiter, get_rate_limit, end_request
from app.services import PredictionClient
from app.utils.logger_client import LoggerClient

bp = Blueprint("api", __name__)

@bp.route("/predict", methods=["POST"])
@start_request  # 📌 1️⃣ Inicia el timer y loggea el inicio de la request
@require_auth   # 📌 2️⃣ Valida autenticación y loggea después de éxito
@limiter.limit(get_rate_limit)  # 📌 3️⃣ Aplica Rate Limiting
@end_request    # 📌 4️⃣ Registra el tiempo total de ejecución
def predict():
    """Endpoint para obtener predicción desde `prediction_service`"""

    inputs = request.json.get("inputs", [])

    if not inputs:
        LoggerClient.error("⚠️Solicitud sin datos de entrada")
        return jsonify({"error": "No input provided"}), 400

    LoggerClient.info(f"📡 Enviando datos al modelo: {inputs}")
    result = PredictionClient.get_prediction(inputs)
    LoggerClient.info(f"🎯 Predicción obtenida: {result}")

    return jsonify(result)