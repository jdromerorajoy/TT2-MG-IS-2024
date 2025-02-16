import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture(autouse=True)
def mock_redis():
    """Mockea Redis para evitar conexión real en los tests."""
    with patch("app.middleware.redis_client", new=MagicMock()):
        yield

@pytest.fixture(scope="session", autouse=True)
def mock_rabbitmq():
    """Mock de RabbitMQ para evitar conexiones reales en los tests."""
    mock_pika = MagicMock()

    # Simulación de la conexión con RabbitMQ
    mock_pika.BlockingConnection.return_value.channel.return_value.basic_publish.return_value = None

    # Aplicamos el mock globalmente en pika.BlockingConnection
    with patch("pika.BlockingConnection", return_value=mock_pika.BlockingConnection()):
        yield mock_pika
