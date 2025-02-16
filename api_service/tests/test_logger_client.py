import pytest
from unittest.mock import patch
from app.utils.logger_client import LoggerClient

@patch("pika.BlockingConnection")
def test_logger_client(mock_pika):
    LoggerClient.info("Test log")

    mock_pika.assert_called_once()