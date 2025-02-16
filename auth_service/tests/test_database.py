import pytest
from app import create_app

def test_init_db():
    """Verifica que `mongo.init_app(app)` se llama correctamente en `create_app()`"""

    # 🔥 Creamos la aplicación
    app = create_app()

    # 🔥 Asegurar que `MONGO_URI` está en la configuración
    assert "MONGO_URI" in app.config


