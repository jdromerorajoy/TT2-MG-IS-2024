import json
import pika
from app.config import Config


class LoggerClient:
    """Cliente para enviar logs a RabbitMQ en lugar de logger_service directamente."""

    @staticmethod
    def log(level, message, service_name="api_service"):
        """Publica logs en RabbitMQ para que logger_service los procese asincrónicamente."""
        try:
            log_data = {
                "level": level,
                "message": message,
                "service": service_name
            }

            # Conectar a RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=Config.RABBITMQ_HOST
            ))
            channel = connection.channel()

            # Declarar la cola de logs
            channel.queue_declare(queue="logs", durable=True)

            # Publicar mensaje en RabbitMQ
            channel.basic_publish(
                exchange="",
                routing_key="logs",
                body=json.dumps(log_data),
                properties=pika.BasicProperties(
                    delivery_mode=2  # Mensaje persistente
                )
            )

            connection.close()

        except Exception as e:
            print(f"⚠️ Error enviando log a RabbitMQ: {e}")

    @staticmethod
    def info(message):
        LoggerClient.log("INFO", message)

    @staticmethod
    def warning(message):
        LoggerClient.log("WARNING", message)

    @staticmethod
    def error(message):
        LoggerClient.log("ERROR", message)