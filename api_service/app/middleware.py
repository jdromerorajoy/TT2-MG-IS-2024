from flask import request, jsonify
import requests

AUTH_SERVICE = "http://auth_service:5001"

def auth_middleware(app):
    @app.before_request
    def validate_api_key():
        api_key = request.headers.get("Authorization")
        if not api_key:
            return jsonify({"error": "API key missing"}), 401

        response = requests.post(f"{AUTH_SERVICE}/validate", json={"api_key": api_key})
        if response.status_code != 200:
            return jsonify({"error": response.json().get('error', 'Unauthorized')}), response.status_code