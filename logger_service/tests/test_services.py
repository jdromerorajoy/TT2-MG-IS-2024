import pytest
from unittest.mock import patch, MagicMock
from app.services import LogService

@patch("app.database.mongo")  # 🔥 Mock de `mongo`
def test_save_log(mock_mongo):
    """Verifica que `save_log()` almacena logs correctamente"""

    # 🔥 Simulamos la colección de logs en MongoDB
    mock_logs_collection = MagicMock()
    mock_mongo.db.logs = mock_logs_collection

    # 🔥 Llamamos a la función que guarda el log
    LogService.save_log("INFO", "Mensaje de prueba", "test_service")

    # ✅ Verificamos que se llamó `insert_one()`
    mock_logs_collection.insert_one.assert_called_once()
    assert mock_logs_collection.insert_one.call_args[0][0]["message"] == "Mensaje de prueba"
