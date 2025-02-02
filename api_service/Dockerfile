# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Crear entorno virtual
RUN python3 -m venv venv

# Configurar PATH para que use venv por defecto
ENV PATH="/app/venv/bin:$PATH"

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 5000

# Ejecutar Gunicorn correctamente
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "app:create_app()"]