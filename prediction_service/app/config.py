import os

class Config:
    """Configuración de Flask y Redis"""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    LOGGER_SERVICE_URL = os.getenv("LOGGER_SERVICE_URL", "http://logger_service:8003")