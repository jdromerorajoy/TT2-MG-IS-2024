import os

class Config:
    """Configuración de Flask y MongoDB"""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/authdb")