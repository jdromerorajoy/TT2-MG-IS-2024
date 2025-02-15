import pytest
from unittest.mock import patch

# Mock para evitar dependencia de logger_service
class LoggerClient:
    @staticmethod
    def info(message):
        pass

    @staticmethod
    def warning(message):
        pass

    @staticmethod
    def error(message):
        pass

@pytest.mark.xfail(reason="LoggerService aún no está implementado")
@patch("app.logger_client.LoggerClient.info", return_value=None)
def test_logger_mock(mock_logger):
    LoggerClient.info("Test log message")
    mock_logger.assert_called_once()
