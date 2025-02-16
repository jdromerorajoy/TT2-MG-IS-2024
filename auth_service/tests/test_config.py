import pytest
from app.config import Config

def test_config():
    assert Config.SECRET_KEY == "supersecret"
    assert Config.MONGO_URI == "mongodb://mongo_auth:27017/auth_db"
    assert Config.LOGGER_SERVICE_URL == "http://logger_service:8003"
    assert Config.RABBITMQ_HOST == "rabbitmq"
    assert Config.RABBITMQ_PORT == 5672