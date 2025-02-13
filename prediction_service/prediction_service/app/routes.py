from flask import Blueprint, request, jsonify, current_app
import torch
from app.model import predict_similarity
from app.utils.logger_client import LoggerClient

bp = Blueprint('prediction', __name__)

@bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = data.get("inputs", [])

    if len(inputs) != 2:
        return jsonify({"error": "Debes enviar exactamente dos conjuntos de propiedades"}), 400

    try:
        # 🔹 Convertir strings de tripletes a listas de enteros
        entity_1 = [list(map(int, triplet.split(","))) for triplet in inputs[0]]
        entity_2 = [list(map(int, triplet.split(","))) for triplet in inputs[1]]

        # 🔹 Convertir a tensores de PyTorch
        tensor_1 = torch.tensor(entity_1, dtype=torch.long)
        tensor_2 = torch.tensor(entity_2, dtype=torch.long)

        redis_client = current_app.redis
        cache_key = f"predict:{inputs[0]}:{inputs[1]}"

        # 🔹 Verificar caché antes de calcular la predicción
        cached_result = redis_client.get(cache_key)
        if cached_result:
            return jsonify({"probabilidad": float(cached_result), "cached": True})

        # 🔹 Usar el modelo real para predecir la similitud
        probabilidad = predict_similarity(tensor_1, tensor_2)

        # 🔹 Guardar en caché por 5 minutos
        redis_client.setex(cache_key, 300, str(probabilidad))

        return jsonify({"probabilidad": probabilidad, "cached": False})

    except Exception as e:
        return jsonify({"error": f"Error procesando la solicitud: {str(e)}"}), 500