#!/bin/bash

# Inicializar la base de datos en segundo plano
python init_db.py &

# Esperar unos segundos para asegurar que MongoDB está listo
sleep 3

# Iniciar Gunicorn con la aplicación Flask correctamente
exec gunicorn --workers 3 --bind 0.0.0.0:8001 "app:app"