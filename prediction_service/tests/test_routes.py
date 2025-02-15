import pytest
from app import create_app

@pytest.fixture
def client():
    """Inicializa Flask en modo test"""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

@pytest.mark.parametrize("auth_key", ["freemium_key", "premium_key"])
def test_predict_route(client, auth_key):
    """Prueba el endpoint /predict con el predictor real"""

    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": [
            ["87441,1,417881", "87441,2,61240", "87441,3,180913", "87441,16,418071"],
            ["87442,1,417881", "87442,2,59480", "87442,3,180913", "87442,16,418071"]
        ]
    }

    response = client.post("/predict", json=payload, headers=headers)

    # Si el test falla, imprimir la respuesta de Flask
    if response.status_code != 200:
        print("\nERROR DETECTADO")
        print(f"Status Code: {response.status_code}")
        print(f"Response Data: {response.data.decode()}")

    assert response.status_code == 200
    assert "probabilidad" in response.json
    assert 0 <= response.json["probabilidad"] <= 1  # Validar que el resultado sea una probabilidad
