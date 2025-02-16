import os

class Config:
    """Configuración de Flask y MongoDB"""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo_logger:27017/logger_db")