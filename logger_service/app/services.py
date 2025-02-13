import logging
from app.database import mongo

# Configurar logging estándar para `logger_service`
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logger_service")

class LogService:
    """Servicio para gestionar logs en MongoDB."""

    @staticmethod
    def save_log(level, message, service):
        """Guarda un log en MongoDB."""
        logger.info(f"📌 level: {level}")
        logger.info(f"📌 message: {message}")
        logger.info(f"📌 service: {service}")

        log_entry = {
            "level": level,
            "message": message,
            "service": service
        }
        try:
            mongo.db.logs.insert_one(log_entry)
            logger.info(f"📌 Log almacenado en MongoDB: {message}")
        except Exception as e:
            logger.error(f"⚠️ Error al guardar log en MongoDB: {e}")