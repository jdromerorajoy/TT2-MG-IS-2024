import requests
from app.config import Config
from app.utils.logger_client import LoggerClient

class PredictionClient:
    """Cliente para comunicarse con `prediction_service`."""

    @staticmethod
    def get_prediction(inputs):
        """Obtiene la predicción desde `prediction_service`."""
        try:
            # Realizar la solicitud a `prediction_service`
            response = requests.post(f"{Config.PREDICTION_SERVICE_URL}/predict", json={"inputs": inputs})
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            LoggerClient.error(f"Error en PredictionClient: {str(e)}")
            return {"error": "Service unavailable"}, 503