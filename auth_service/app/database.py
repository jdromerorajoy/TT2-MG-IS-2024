from flask_pymongo import PyMongo
from app.config import Config
from app.utils.logger_client import LoggerClient

mongo = PyMongo()

def init_db(app):
    """Inicializa la base de datos MongoDB"""
    app.config["MONGO_URI"] = Config.MONGO_URI
    try:
        mongo.init_app(app)
        LoggerClient.info("MongoDB conectado correctamente")
    except Exception as e:
        LoggerClient.error(f"Error al conectar con MongoDB: {str(e)}")