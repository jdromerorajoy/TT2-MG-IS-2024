import pytest
from unittest.mock import MagicMock
import sys

# 🔥 FORZAR EL MOCK ANTES DE IMPORTAR `mongo`
mock_db = MagicMock()
mock_collection = MagicMock()

# Simular `find_one` para devolver datos falsos en lugar de conectar a MongoDB
def mock_find_one(query):
    if query.get("api_key") == "freemium_key":
        return {"api_key": "freemium_key", "subscription": "FREEMIUM"}
    elif query.get("api_key") == "premium_key":
        return {"api_key": "premium_key", "subscription": "PREMIUM"}
    return None  # API Key inválida

mock_collection.find_one.side_effect = mock_find_one
mock_db.api_keys = mock_collection

# 🔥 Agregar `mock_db` ANTES de importar `mongo`
sys.modules["app.database"] = MagicMock()
sys.modules["app.database"].mongo.db = mock_db

# Ahora importamos mongo
from app.database import mongo

@pytest.fixture(scope="session", autouse=True)
def mock_mongo():
    """Mock de MongoDB para evitar conexión real en los tests."""
    mock_db = MagicMock()
    mock_collection = MagicMock()

    # 🔥 Aseguramos que `find_one()` devuelva un diccionario real
    def mock_find_one(query):
        if query.get("api_key") == "freemium_key":
            return {"api_key": "freemium_key", "subscription": "FREEMIUM"}
        elif query.get("api_key") == "premium_key":
            return {"api_key": "premium_key", "subscription": "PREMIUM"}
        return None  # 🔥 Caso de API Key inválida

    mock_collection.find_one.side_effect = mock_find_one
    mock_db.api_keys = mock_collection

    # 🔥 Sobrescribimos `mongo.db` con el mock
    mongo.db = mock_db

    return mock_db

