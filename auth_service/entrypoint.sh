#!/bin/bash

python init_db.py &

sleep 3

# Iniciar Gunicorn en segundo plano
gunicorn --workers 3 --bind 0.0.0.0:8001 "app:create_app"
