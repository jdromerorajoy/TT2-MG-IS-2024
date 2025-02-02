from flask import Blueprint, request, jsonify
import requests

bp = Blueprint('api', __name__)

PREDICTION_SERVICE = "http://prediction_service:5002"

@bp.route('/predict', methods=['POST'])
def predict():
    inputs = request.json.get('inputs', [])
    if not inputs:
        return jsonify({"error": "No input provided"}), 400

    response = requests.post(f"{PREDICTION_SERVICE}/predict", json={"inputs": inputs})
    return response.json(), response.status_code