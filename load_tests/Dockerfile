FROM locustio/locust

WORKDIR /load_tests

# Instalar dependencias con caché
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto del servicio
EXPOSE 8089


