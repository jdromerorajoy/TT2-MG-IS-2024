import logging
from flask_pymongo import PyMongo
from app.config import Config

# Inicializa la conexión con MongoDB
mongo = PyMongo()

# Configurar logging local para errores en la base de datos
logging.basicConfig(level=logging.INFO)
db_logger = logging.getLogger("database")

def init_db(app):
    """Configura MongoDB con la aplicación Flask."""
    try:
        app.config["MONGO_URI"] = Config.MONGO_URI
        print("🔥 init_db() fue llamado")
        mongo.init_app(app)
        db_logger.info("✅ Conexión con MongoDB establecida correctamente")
    except Exception as e:
        db_logger.error(f"❌ Error al conectar con MongoDB: {e}")