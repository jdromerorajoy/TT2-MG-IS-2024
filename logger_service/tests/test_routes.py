import pytest
from unittest.mock import patch
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

@patch("app.services.LogService.get_data", return_value={"data": "Success"})  # 🔥 Mock de `get_data()`
def test_get_data(mock_service, client):
    """Verifica que la API responde correctamente en /data"""

    response = client.get("/data")  # 🔥 Simula la petición a la API

    assert response.status_code == 200
    assert response.json == {"data": "Success"}  # ✅ Verifica la respuesta
