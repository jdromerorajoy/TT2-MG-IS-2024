from flask import Flask
from flask_pymongo import PyMongo
from app.routes import bp
from app.config import Config

mongo = PyMongo()

def create_app():
    """Inicializa la aplicación Flask y configura MongoDB"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar MongoDB
    mongo.init_app(app)

    # Agregar MongoDB a la aplicación para que sea accesible en routes.py
    app.mongo = mongo

    app.register_blueprint(bp)
    return app