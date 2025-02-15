from flask import Flask
from app.routes import bp
from app.middleware import limiter


def create_app():
    """Inicializa Flask"""
    app = Flask(__name__)
    app.register_blueprint(bp)

    # Aplicar Rate Limiting a todas las rutas
    limiter.init_app(app)

    return app