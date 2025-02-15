# 🏗️ Arquitectura de Microservicios con Flask, RabbitMQ y MongoDB

Este proyecto implementa una **API de predicción** con **autenticación basada en API Keys**, **limitación de solicitudes** y **registro de logs de manera asíncrona** mediante **RabbitMQ**. Está diseñado bajo una arquitectura de **microservicios** utilizando **Flask, MongoDB, Redis y Docker**.

---

## 📌 Índice

1. [🔧 Características principales](#características-principales)
2. [📂 Estructura del proyecto](#estructura-del-proyecto)
3. [🚀 Instalación y configuración](#instalación-y-configuración)
4. [🔄 Flujo de trabajo](#flujo-de-trabajo)
5. [📝 Endpoints disponibles](#endpoints-disponibles)
6. [📊 Pruebas y monitoreo](#pruebas-y-monitoreo)
7. [👨‍💻 Contribuir](#contribuir)
8. [📄 Licencia](#licencia)

---

## 🔧 Características principales

✔️ **Autenticación con API Key** (Freemium/Premium)\
✔️ **Rate limiting** para controlar el número de solicitudes por tipo de suscripción\
✔️ **Cache con Redis** para mejorar el rendimiento\
✔️ **RabbitMQ para logs asíncronos**\
✔️ **MongoDB como base de datos principal**\
✔️ **Arquitectura modular basada en microservicios**\
✔️ **Pruebas de carga con Locust**\
✔️ **Docker Compose para fácil despliegue**

---

## 📂 Estructura del proyecto

```
├── microservices/
│   ├── api_service/          # Servicio API principal
│   ├── auth_service/         # Servicio de autenticación
│   ├── prediction_service/   # Servicio de predicción
│   ├── logger_service/       # Servicio de logs
│   ├── load_tests/           # Pruebas de carga con Locust
│   ├── rabbitmq/             # Configuración de RabbitMQ
│
├── docker-compose.yml        # Orquestación de contenedores
├── README.md                 # Documentación del proyecto
└── .env                      # Variables de entorno
```

---

## 🚀 Instalación y configuración

### ✅ Requisitos previos

Antes de empezar, asegúrate de tener instalados:

- **Docker** y **Docker Compose**
- **Python 3.9+**
- **Postman** (opcional para pruebas de API)

### ⚙️ Pasos para ejecutar el proyecto

1️⃣ **Clonar el repositorio**

```sh
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2️⃣ **Levantar los contenedores con Docker**

```sh
docker-compose up --build -d
```

3️⃣ **Verificar que los servicios estén corriendo**

```sh
docker ps
```

4️⃣ **Ver logs de algún servicio**

```sh
docker-compose logs -f api_service
```

5️⃣ **Probar la API con Postman o cURL**

---

## 🔄 Flujo de trabajo

1. El **cliente** realiza una petición `POST /predict` con su **API Key**.
2. El **Auth Service** valida la API Key y determina el nivel de suscripción (`freemium` o `premium`).
3. El **Rate Limiter** restringe el número de solicitudes según la suscripción.
4. La API consulta el **cache en Redis** para respuestas rápidas.
5. Si no está en caché, el **Prediction Service** ejecuta el modelo y guarda la respuesta.
6. Todos los eventos se registran en **RabbitMQ** y son procesados asíncronamente por el **Logger Service**.

---

## 📝 Endpoints disponibles

### 🔐 Autenticación

#### `POST /validate`

**Descripción:** Verifica si la API Key es válida.\
**Ejemplo de petición:**

```sh
curl -X POST http://localhost:8001/validate \
     -H "Content-Type: application/json" \
     -d '{"api_key": "freemium_key"}'
```

**Respuesta esperada:**

```json
{"valid": true}
```

---

### 🔮 Predicción

#### `POST /predict`

**Descripción:** Retorna la probabilidad de similitud entre dos entidades.\
**Ejemplo de petición:**

```sh
curl -X POST http://localhost:8000/predict \
     -H "Authorization: premium_key" \
     -H "Content-Type: application/json" \
     -d '{"inputs": ["87441,1,417881", "87442,1,417881"]}'
```

**Respuesta esperada:**

```json
{
  "probabilidad": 0.87,
  "cached": false
}
```

---

### 📜 Logs

#### `GET /logs`

**Descripción:** Recupera los logs almacenados en MongoDB.\
**Ejemplo:**

```sh
curl -X GET http://localhost:8003/logs
```

---

## 📊 Pruebas y monitoreo

### 🔥 Pruebas de carga con Locust

Para evaluar el rendimiento y límites del API:

1. Levantar Locust:
   ```sh
   docker-compose up locust
   ```
2. Acceder a `http://localhost:8089`
3. Configurar el número de usuarios y tasa de spawn.
4. Iniciar la prueba y analizar resultados.

---

## 👨‍💻 Contribuir

Si deseas contribuir:

1. Haz un **fork** del repositorio.
2. Crea una **nueva rama** (`feature-nueva-funcionalidad`).
3. Realiza tus cambios y **haz un commit**.
4. Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la **MIT License**.

