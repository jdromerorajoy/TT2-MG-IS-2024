import pytest
from unittest.mock import MagicMock

@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    """Mock de Redis para evitar errores de conexión en los tests."""
    mock_redis_client = MagicMock()
    
    # Simular las funciones de Redis
    mock_redis_client.get.return_value = None
    mock_redis_client.set.return_value = None

    monkeypatch.setattr("app.redis_client", mock_redis_client)
    return mock_redis_client


