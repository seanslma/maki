# Redis-py

## install redis-py
`redis-py` client for Redis
```sh
pip install redis[hiredis]
mamba install redis-py hiredis
```

## methods
`time` can be represented by int or a Python timedelta/datetime object
- `r.setx(key, time, value)`
  set value of key that expires in time seconds
- `r.expire(key, time)`
  set expire flag for time seconds
- `r.psetex(key, time_ms, value)`
  set value of key that expires in time_ms milliseconds
- `r.expireat(key, when)`
  set an expire flag
- `r.persist(key)`
  remove expiration
- `r.ttl(key)`
  return the number of seconds until the key expires
- `r.pttl(key)`
  return the number of milliseconds until the key expires

## create server
```py
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
print(r.ping())
print(r.keys("*"))
```

## connetect to local/cluster
```py
from redis.cluster import RedisCluster

# `decode_responses=True` convert return value from bytes to str.
#r = redis.Redis(host='localhost', port=6379, decode_responses=True)
rc = RedisCluster(host='localhost', port=16379)

print(rc.get_nodes())
# [[host=127.0.0.1,port=16379,name=127.0.0.1:16379,server_type=primary,
#  redis_connection=Redis<ConnectionPool<Connection<host=127.0.0.1,port=16379,db=0>>>], ...
```

## connect with tls
```py
import redis

r = redis.Redis(
    host="my-redis.cloud.redislabs.com",
    port=6379,
    username="default", # use your Redis user. More info https://redis.io/docs/management/security/acl/
    password="secret", # use your Redis password
    ssl=True,
    ssl_certfile="./redis_user.crt",
    ssl_keyfile="./redis_user_private.key",
    ssl_ca_certs="./redis_ca.pem",
)
```

## examples
```py
r.set('key', 'val')
r.get('key')

dv = {
    'a': 'x',
    'b': 'y'
}
r.mset(dv)
r.get('b')

lv = ['a', 'b']
r.sadd('lv', *lv)
r.smembers('lv')

lv = ['x', 'y']
r.lpush('lp', *lv)
r.lrange('lp', 0, -1)

import json
jv = {
    'name': 'John',
    'age': 20,
    'address':{
        'number': 19,
        'street': 'Goldey',
        'suburb': 'Cuddly'
    },
    'skills': ['art', 'math']
}
r.set('jv', json.dumps(jv))
json.loads(r.get('jv'))
```

## difference between redis.Redis and redis.StrictRedis
In the `redis-py` library, both `redis.Redis` and `redis.StrictRedis` are classes that provide a client interface
for interacting with a Redis server. However, there is a subtle historical difference between them.

1. **`redis.Redis` (Deprecated):**
   - `redis.Redis` was the original class in `redis-py` for creating a Redis client.
   - Over time, the developers realized that the name `StrictRedis` better reflects the fact that the library adheres strictly to the official Redis command syntax.
   - To avoid confusion, `StrictRedis` was introduced, and it was recommended to use `StrictRedis` instead of `Redis`. As a result, `Redis` is now deprecated.

2. **`redis.StrictRedis` (Recommended):**
   - `redis.StrictRedis` is the replacement for `redis.Redis` and is the recommended class to use in modern code.
   - It provides a clean and consistent API, strictly following the official Redis command syntax.
   - `StrictRedis` is more feature-complete, and its usage is considered best practice.

**Usage:**
```py
# Recommended: Use StrictRedis
import redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Deprecated: Avoid using Redis
# import redis
# redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
```

In summary, while both `redis.Redis` and `redis.StrictRedis` can be used, it's strongly recommended to use `redis.StrictRedis`
in modern code to take advantage of the latest features, improvements, and best practices.
If you encounter existing code that uses `redis.Redis`, consider updating it to use `redis.StrictRedis`.
