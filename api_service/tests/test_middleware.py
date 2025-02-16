import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from app.middleware import require_auth, start_request, end_request

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True

    @app.route("/protected")
    @require_auth
    def protected():
        return jsonify({"message": "Access granted"}), 200

    return app.test_client()

@patch("requests.post")
def test_require_auth_valid_key(mock_post, client):
    mock_post.return_value.status_code = 200

    response = client.get("/protected", headers={"Authorization": "valid_key"})
    assert response.status_code == 200
    assert response.json["message"] == "Access granted"

def test_require_auth_missing_key(client):
    response = client.get("/protected")
    assert response.status_code == 401
