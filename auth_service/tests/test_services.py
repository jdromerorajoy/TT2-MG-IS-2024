import pytest
from unittest.mock import patch
from app.services import AuthService

@patch("app.database.mongo.db.api_keys.find_one")
def test_auth_service(mock_find_one):
    mock_find_one.return_value = {"api_key": "freemium_key", "subscription": "FREEMIUM"}
    response, status = AuthService.validate_api_key("freemium_key")
    assert status == 200
    assert response == {"valid": True, "subscription": "FREEMIUM"}

    mock_find_one.return_value = None
    response, status = AuthService.validate_api_key("invalid_key")
    assert status == 403
    assert "error" in response