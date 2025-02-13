from app.database import mongo
from app.utils.logger_client import LoggerClient


class AuthService:
    """Manejo de autenticación y validación de API Keys"""

    @staticmethod
    def validate_api_key(api_key):
        if not api_key:
            return {"error": "API key missing"}, 401

        user = mongo.db.users.find_one({"api_key": api_key})
        if not user:
            LoggerClient.warning(f"Intento de acceso con API key inválida: {api_key}")
            return {"error": "Unauthorized"}, 401

        return {"status": "Valid API key"}, 200