import pytest 
from app import create_app
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

@pytest.mark.parametrize("api_key, expected_status", [
    ("freemium_key", 200),
    ("premium_key", 200),
    ("invalid_key", 403)
])
def test_validate_api_key(client, api_key, expected_status):
    response = client.post("/validate", json={"api_key": api_key})
    assert response.status_code == expected_status