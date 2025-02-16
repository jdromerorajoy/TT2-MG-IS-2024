import pytest
from app.config import Config

def test_config():
    assert Config.SECRET_KEY == "supersecret"
    assert Config.REDIS_HOST == "redis"
    assert Config.REDIS_PORT == 6379
    assert Config.LOGGER_SERVICE_URL == "http://logger_service:8003"
