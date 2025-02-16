import os

class Config:
    """Configuración central del servicio"""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo_auth:27017/auth_db")

    LOGGER_SERVICE_URL = os.getenv("LOGGER_SERVICE_URL", "http://logger_service:8003")
    RABBITMQ_HOST = "rabbitmq"
    RABBITMQ_PORT = 5672
    RABBITMQ_USER = "user"
    RABBITMQ_PASSWORD = "password"