from flask import Flask
from app.routes import bp
from app.middleware import limiter
from app.utils.logger_client import LoggerClient
import os


def create_app():
    """Inicializa Flask"""
    app = Flask(__name__)
    app.register_blueprint(bp)

    # Aplicar Rate Limiting a todas las rutas
    limiter.init_app(app)

    if os.getpid() == 1:  # Solo se ejecuta en el proceso maestro de Gunicorn
        LoggerClient.info("API Service iniciado")

    return app