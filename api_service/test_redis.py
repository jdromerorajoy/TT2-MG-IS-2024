import redis

try:
    client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
    pong = client.ping()
    print(f"✅ Conexión exitosa a Redis: {pong}")
except Exception as e:
    print(f"🚨 Error conectando a Redis: {e}")
