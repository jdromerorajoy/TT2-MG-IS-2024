from locust import HttpUser, task, between, events
import logging

# Configurar logging para registrar respuestas 429 (Rate Limit Exceeded)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseUser(HttpUser):
    """Clase base para usuarios (debe ser abstracta para evitar errores)"""
    abstract = True  # 🔹 Evita que Locust intente ejecutar esta clase directamente
    wait_time = between(1, 3)  # Simula pausas entre requests para hacer ramp-up

    def predict(self, api_key):
        """Realiza una solicitud al endpoint /predict con la API Key dada"""
        headers = {"Authorization": api_key, "Content-Type": "application/json"}
        payload = {
            "inputs": [["87441,1,417881", "87441,2,61240", "87441,3,180913", "87441,16,418071"],
                       ["87442,1,417881", "87442,2,59480", "87442,3,180913", "87442,16,418071"]]
        }
        response = self.client.post("http://api_service:8000/predict", json=payload, headers=headers)

        if response.status_code == 429:
            logger.warning(f"⚠️ Rate Limit Exceeded ({api_key}): {response.text}")

    def on_start(self):
        """Ejecutado cuando el usuario inicia la simulación"""
        logger.info(f"🚀 Usuario iniciado: {self.__class__.__name__}")

class FreemiumUser(BaseUser):
    """Usuario con suscripción Freemium (Límite de 5 requests por minuto)"""
    @task
    def predict_freemium(self):
        self.predict("freemium_key")

class PremiumUser(BaseUser):
    """Usuario con suscripción Premium (Límite de 50 requests por minuto)"""
    @task
    def predict_premium(self):
        self.predict("premium_key")

# Registrar eventos para monitoreo
@events.request.add_listener
def log_response(request_type, name, response_time, response_length, response, **kwargs):
    """Captura respuestas HTTP y loggea Rate Limit Exceeded"""
    if response.status_code == 429:
        logger.warning(f"🚨 RATE LIMIT EXCEEDED: {name} ({response.status_code})")