import pytest
from unittest.mock import patch
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

@patch("requests.post")
@patch("app.services.PredictionClient.get_prediction", return_value={"prediction": 0.85})
def test_predict(mock_prediction, mock_auth, client):
    """Prueba la ruta /predict con autenticación mockeada"""

    # 🔥 Simulamos una respuesta exitosa de auth_service
    mock_auth.return_value.status_code = 200
    mock_auth.return_value.json.return_value = {"valid": True, "subscription": "FREEMIUM"}

    headers = {"Authorization": "freemium_key", "Content-Type": "application/json"}
    payload = {"inputs": [["data1"], ["data2"]]}

    response = client.post("/predict", json=payload, headers=headers)

    assert response.status_code == 200
    assert "prediction" in response.json
    assert response.json["prediction"] == 0.85
