from flask import Flask
from app.routes import bp
from app.config import Config

def create_app():
    """Inicializa la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(bp)

    return app