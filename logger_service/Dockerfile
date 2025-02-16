FROM python:3.9-slim

WORKDIR /app
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Asegurar que `app` esté en el PYTHONPATH
ENV PYTHONPATH="/app"

# Agregar permisos de ejecución al script de entrypoint
RUN chmod +x /app/entrypoint.sh

EXPOSE 8003

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]