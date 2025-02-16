from unittest.mock import patch
from app import create_app

@patch("app.database.init_db")  # ✅ Mockeamos `init_db` en `app.database`
def test_init_db(mock_init_db):
    """Verifica que `init_db` se llama correctamente en `create_app()`"""

    app = create_app()

    # ✅ Verificar que `MONGO_URI` está en la configuración
    assert "MONGO_URI" in app.config

    # ✅ Verificar que `init_db(app)` fue llamado UNA VEZ
    mock_init_db.assert_called_once_with(app)
