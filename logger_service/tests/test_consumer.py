import pytest
import json
from unittest.mock import patch, MagicMock
from consumer import callback

@pytest.fixture
def sample_log():
    """Ejemplo de log para probar la callback de RabbitMQ"""
    return json.dumps({"level": "INFO", "message": "Test log", "service": "logger_service"}).encode()

@patch("consumer.logs_collection")
def test_callback(mock_logs_collection, sample_log):
    """Verifica que los logs sean almacenados correctamente en MongoDB"""
    ch = MagicMock()
    method = MagicMock()
    properties = MagicMock()

    # Llamar al callback con el mensaje de prueba
    callback(ch, method, properties, sample_log)

    # Verificar que insert_one fue llamado en MongoDB
    mock_logs_collection.insert_one.assert_called_once()
    assert mock_logs_collection.insert_one.call_args[0][0]["message"] == "Test log"

    # Verificar que se confirmó la recepción del mensaje en RabbitMQ
    ch.basic_ack.assert_called_once_with(delivery_tag=method.delivery_tag)
