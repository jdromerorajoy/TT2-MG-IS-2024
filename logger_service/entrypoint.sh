#!/bin/bash

# Iniciar Gunicorn en segundo plano
gunicorn --workers 3 --bind 0.0.0.0:8003 "app:create_app" &

# Esperar 3 segundos para asegurar que Gunicorn esté activo
sleep 3

# Iniciar el consumidor de RabbitMQ
exec python consumer.py