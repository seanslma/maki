# Redis

## check redis server availability
```py
import redis

def check_redis_availability():
    # Create a StrictRedis instance
    redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    try:
        # Ping the Redis server
        response = redis_client.ping()
    except Exception as e:
        print(f'Error checking Redis availability: {e}')
    else:
        if response:
            print('Redis server is available.')
        else:
            print('Redis server did not respond to PING.')

# Check if Redis server is available
check_redis_availability()
```
