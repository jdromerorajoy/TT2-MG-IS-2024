import pytest
from unittest.mock import patch

@patch("app.utils.logger_client.LoggerClient")
def test_logger_client(mock_logger):
    from app.utils.logger_client import LoggerClient
    LoggerClient.info("Test log message")
    mock_logger.info.assert_called()