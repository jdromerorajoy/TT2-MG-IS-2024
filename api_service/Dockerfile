# Imagen base optimizada
FROM python:3.9-slim

# Definir el directorio de trabajo
WORKDIR /app

# Instalar dependencias con caché
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto del servicio
EXPOSE 8000

# Comando de inicio
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:create_app()"]