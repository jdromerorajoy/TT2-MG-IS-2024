import os

class Config:
    """Configuración de Flask"""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")