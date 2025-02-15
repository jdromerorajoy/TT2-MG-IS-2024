import os
from redis import Redis

class Config:
    """Configuración del servicio"""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth_service:8001")
    PREDICTION_SERVICE_URL = os.getenv("PREDICTION_SERVICE_URL", "http://prediction_service:8002")

    # Configuración de Redis para caché
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))

    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

    LOGGER_SERVICE_URL = os.getenv("LOGGER_SERVICE_URL", "http://logger_service:8003")
    RABBITMQ_HOST = "rabbitmq"
    RABBITMQ_PORT = 5672
    RABBITMQ_USER = "user"
    RABBITMQ_PASSWORD = "password"