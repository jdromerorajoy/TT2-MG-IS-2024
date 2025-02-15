from flask import Flask
from app.routes import bp
from app.database import init_db
from app.utils.logger_client import LoggerClient

def create_app():
    """Inicializa Flask con MongoDB"""
    app = Flask(__name__)

    init_db(app)  # Conectar MongoDB
    app.register_blueprint(bp)

    #LoggerClient.info("Auth Service iniciado correctamente")
    return app