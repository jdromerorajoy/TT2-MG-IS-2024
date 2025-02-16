import pytest
from unittest.mock import patch, MagicMock
from app import create_app

@pytest.fixture
def client():
    """Fixture para configurar un cliente de pruebas de Flask."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_database():
    """Mock para la base de datos."""
    with patch("app.database.init_db") as mock_db:
        yield mock_db

@pytest.fixture
def mock_services():
    """Mock para los servicios."""
    with patch("app.services.some_service_method") as mock_service:
        yield mock_service

@pytest.fixture
def mock_consumer():
    """Mock para el consumidor de mensajes."""
    with patch("app.consumer.Consumer.process_message") as mock_consumer:
        yield mock_consumer