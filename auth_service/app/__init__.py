# from flask import Flask
# from app.routes import bp
# from app.database import init_db
# from app.utils.logger_client import LoggerClient

# def create_app():
#     """Inicializa Flask con MongoDB"""
#     app = Flask(__name__)

#     init_db(app)  # Conectar MongoDB
#     app.register_blueprint(bp)

#     #LoggerClient.info("Auth Service iniciado correctamente")
#     return app

from flask import Flask
from app.routes import bp
from app.database import mongo  # 🔥 Asegúrate de importar `mongo`
from app.database import init_db
from app.config import Config  # 🔥 Importar configuración

def create_app():
    """Inicializa Flask con MongoDB"""
    app = Flask(__name__)

    # 🔥 Asegurar que la configuración se carga antes de inicializar la BD
    app.config.from_object(Config)

    # 🔥 Llamar `init_app()` correctamente
    init_db(app)  

    app.register_blueprint(bp)
    
    return app
