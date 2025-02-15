import os
import requests
import time
from flask import request, jsonify, g
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.utils.logger_client import LoggerClient

# Inicializar Rate Limiter con Redis
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=os.getenv("REDIS_URL", "redis://redis:6379")
)

def start_request(f):
    """Middleware para registrar inicio de la request"""
    def wrapper(*args, **kwargs):
        g.start_time = time.time()  # Capturar tiempo de inicio
        LoggerClient.info("⏳ Inicio de request...")  # Log al inicio
        return f(*args, **kwargs)
    return wrapper


def require_auth(f):
    """Middleware de autenticación basado en API Key"""
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("Authorization")
        if not api_key:
            return jsonify({"error": "Missing API Key"}), 401

        response = requests.post(f"{os.getenv('AUTH_SERVICE_URL', 'http://auth_service:8001')}/validate",
                                 json={"api_key": api_key})

        if response.status_code != 200:
            return jsonify({"error": "Unauthorized"}), 403

        return f(*args, **kwargs)

    return wrapper

def get_rate_limit():
    """Determina el límite de solicitudes basado en la API Key"""
    api_key = request.headers.get("Authorization", "")
    return "50 per minute" if api_key == "premium_key" else "5 per minute"

def end_request(f):
    """Middleware para registrar el tiempo total de ejecución"""
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        elapsed_time = time.time() - g.start_time
        LoggerClient.info(f"⏳ Tiempo total de ejecución: {elapsed_time:.4f} segundos")
        return response
    return wrapper