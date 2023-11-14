# Redis

## check redis server availability
```py
import redis

def check_redis_availability():
    try:
        redis_host = 'localhost'
        redis_port = 6379

        # Create a StrictRedis instance
        redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

        # Ping the Redis server
        response = redis_client.ping()

        if response:
            print("Redis server is available.")
        else:
            print("Redis server did not respond to PING.")
    except Exception as e:
        print(f"Error checking Redis availability: {e}")

# Check if Redis server is available
check_redis_availability()
```
