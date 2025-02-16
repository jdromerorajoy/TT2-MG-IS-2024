import pika
import json
import time
import logging
from pymongo import MongoClient
from datetime import datetime

# Configurar logger estándar
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurar conexión a MongoDB
MONGO_URI = "mongodb://mongo_logger:27017/logger_db"  # Asegúrate de usar el puerto correcto
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["logger_db"]
logs_collection = mongo_db["logs"]

# Configurar credenciales para RabbitMQ
RABBITMQ_USER = "user"  # Reemplaza con tu usuario
RABBITMQ_PASSWORD = "password"  # Reemplaza con tu contraseña
RABBITMQ_HOST = "rabbitmq"  # Nombre del contenedor o IP del RabbitMQ
RABBITMQ_QUEUE = "logs"

def connect_to_rabbitmq():
    """Intenta conectarse a RabbitMQ con autenticación y reintentos."""
    max_retries = 10
    retry_delay = 5  # Segundos entre reintentos

    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)

    for attempt in range(max_retries):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=RABBITMQ_HOST,
                    credentials=credentials,
                    heartbeat=600,  # Mantener conexión viva
                    blocked_connection_timeout=300
                )
            )
            logger.info("✅ Conexión exitosa con RabbitMQ.")
            return connection
        except pika.exceptions.AMQPConnectionError:
            logger.warning(f"⚠️ RabbitMQ no está disponible. Reintentando en {retry_delay} segundos...")
            time.sleep(retry_delay)

    raise RuntimeError("❌ No se pudo conectar a RabbitMQ después de múltiples intentos.")

def callback(ch, method, properties, body):
    """Procesa los mensajes de la cola de RabbitMQ y los guarda en MongoDB"""
    log_entry = json.loads(body)
    log_entry["timestamp"] = datetime.utcnow().isoformat()
    logger.info(f"📌 Log recibido: {log_entry}")

    try:
        if logs_collection is not None:
            logs_collection.insert_one(log_entry)
            logger.info("📌 Log almacenado en MongoDB")
        else:
            logger.error("❌ Conexión a MongoDB no inicializada.")
    except Exception as e:
        logger.error(f"⚠️ Error al guardar log en MongoDB: {e}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume_logs():
    """Consume logs de la cola `logs` en RabbitMQ"""
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)
    logger.info("📌 Logger Service esperando logs en RabbitMQ...")

    channel.start_consuming()

if __name__ == "__main__":
    consume_logs()