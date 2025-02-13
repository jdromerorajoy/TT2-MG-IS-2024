from flask import Flask
from redis import Redis
from app.routes import bp
from app.config import Config

redis_client = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

def create_app():
    """Inicializa Flask con Redis"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.redis = redis_client

    app.register_blueprint(bp)
    return app