from flask import Blueprint, request, jsonify, current_app

bp = Blueprint('auth', __name__)

API_KEYS = {"freemium_key": "FREEMIUM", "premium_key": "PREMIUM"}
LIMITS = {"FREEMIUM": 5, "PREMIUM": 50}

@bp.route('/validate', methods=['POST'])
def validate():
    """Valida la API Key y aplica rate limiting"""
    api_key = request.json.get('api_key')
    if api_key not in API_KEYS:
        return jsonify({"error": "Invalid API key"}), 401

    # Usar current_app.mongo en lugar de importar mongo directamente
    mongo = current_app.mongo

    user = mongo.db.users.find_one({"api_key": api_key})
    if not user:
        mongo.db.users.insert_one({"api_key": api_key, "requests": 0, "plan": API_KEYS[api_key]})
        user = {"api_key": api_key, "requests": 0, "plan": API_KEYS[api_key]}

    requests_count = user['requests']
    if requests_count >= LIMITS[user['plan']]:
        return jsonify({"error": "Rate limit exceeded"}), 429

    mongo.db.users.update_one({"api_key": api_key}, {"$inc": {"requests": 1}})
    return jsonify({"status": "Valid API key"}), 200