import pymongo
import os
import time

# Configurar la conexión a MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo_auth:27017/")
DB_NAME = "auth_db"

# Intentar conectar a MongoDB con reintentos
client = None
max_retries = 10
for attempt in range(max_retries):
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        print("✅ Conexión exitosa con MongoDB")
        break
    except Exception as e:
        print(f"⚠️ Intento {attempt + 1}/{max_retries} - Error al conectar a MongoDB: {e}")
        time.sleep(5)  # Esperar 5 segundos antes de reintentar

if client is None:
    print("❌ No se pudo conectar a MongoDB después de varios intentos. Abortando.")
    exit(1)

# Colección de API Keys
api_keys_collection = db["auth"]

# Datos predefinidos
default_keys = [
    {"api_key": "freemium_key", "subscription": "FREEMIUM"},
    {"api_key": "premium_key", "subscription": "PREMIUM"}
]

# Insertar solo si la colección está vacía
if api_keys_collection.count_documents({}) == 0:
    api_keys_collection.insert_many(default_keys)
    print("✅ API Keys insertadas correctamente en MongoDB")
else:
    print("⚠️ API Keys ya existen en la base de datos, no se insertaron nuevamente.")

client.close()