import pika
import json
import logging
from app.config import Config

# Configurar logger estándar para debug
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoggerClient:
    """Cliente para enviar logs a RabbitMQ"""

    @staticmethod
    def log(level, message, service_name="api_service"):
        """Envía logs a RabbitMQ en lugar de llamar directamente a `logger_service`."""
        try:
            # Establecer conexión con RabbitMQ
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=Config.RABBITMQ_HOST,
                    port=Config.RABBITMQ_PORT,
                    credentials=pika.PlainCredentials(Config.RABBITMQ_USER, Config.RABBITMQ_PASSWORD)
                )
            )
            channel = connection.channel()

            # Declarar la cola para asegurarnos de que existe
            channel.queue_declare(queue="logs", durable=True)

            # Crear el mensaje en formato JSON
            log_data = {
                "level": level,
                "message": message,
                "service": service_name
            }
            message = json.dumps(log_data)

            # Publicar mensaje en la cola
            channel.basic_publish(
                exchange="",
                routing_key="logs",
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2  # Hace que el mensaje sea persistente
                )
            )

            logger.info(f"📌 Log enviado a RabbitMQ: {message}")

            # Cerrar la conexión
            connection.close()

        except Exception as e:
            logger.error(f"⚠️ Error enviando log a RabbitMQ: {e}")

    @staticmethod
    def info(message):
        LoggerClient.log("INFO", message)

    @staticmethod
    def warning(message):
        LoggerClient.log("WARNING", message)

    @staticmethod
    def error(message):
        LoggerClient.log("ERROR", message)