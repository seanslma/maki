# Redis

## Python app
```py
import redis

# Connect to Redis using the service name and port
redis_client = redis.StrictRedis(host='redis-service', port=6379, decode_responses=True)

# Example: set and get a key
redis_client.set('example_key', 'example_value')
value = redis_client.get('example_key')
print(f'Redis Value: {value}')
```

## service
The service selects pods with the label `app: standalone-redis`

## redis
set memory limit
```yaml
containers:
  - name: redis
    image: public.ecr.aws/docker/library/redis:7.0.4-alpine
    ports:
      - containerPort: 6379
    command: ["redis-server"]
    args: ["--save", "", "--appendonly", "no", "--maxmemory", "8G"]
```
