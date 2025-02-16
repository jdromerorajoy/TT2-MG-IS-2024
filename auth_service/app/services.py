from app.database import mongo
from app.utils.logger_client import LoggerClient

class AuthService:
    """Manejo de autenticación y validación de API Keys"""

    @staticmethod
    def validate_api_key(api_key):
        """Valida la API Key desde MongoDB"""
        if not api_key:
            return {"error": "API key missing"}, 401

        user = mongo.db.api_keys.find_one({"api_key": api_key})
        if not user:
            LoggerClient.warning(f"🚫 Intento de acceso con API key inválida: {api_key}")
            return {"error": "Unauthorized"}, 403

        LoggerClient.info(f"✅ Autenticación exitosa para API Key: {api_key}")
        return {"valid": True, "subscription": user["subscription"]}, 200