from flask import Flask
from app.routes import bp
from app.middleware import auth_middleware

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    auth_middleware(app)
    app.register_blueprint(bp)

    return app