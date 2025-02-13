from flask import Flask
from app.routes import bp
from app.config import Config
from app.database import mongo, init_db



def create_app():
    """Inicializa la aplicación Flask y la conexión a MongoDB"""
    app = Flask(__name__)

    init_db(app)

    app.register_blueprint(bp)

    return app