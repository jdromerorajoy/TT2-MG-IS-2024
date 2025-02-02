from flask import Blueprint, request, jsonify
from app.model import predict_similarity

bp = Blueprint('prediction', __name__)

@bp.route('/predict', methods=['POST'])
def predict():
    """Recibe dos subgrafos y devuelve la probabilidad de que sean similares"""
    data = request.json
    inputs = data.get("inputs", [])

    if len(inputs) != 2:
        return jsonify({"error": "Debes enviar exactamente dos subgrafos"}), 400

    probabilidad = predict_similarity(inputs[0], inputs[1])
    return jsonify({"probabilidad": probabilidad})