# Redis-py
https://redis.io/docs/clients/python/

## install redis-py
`redis-py` client for Redis
```
pip install redis[hiredis]
```

## connetect to local/cluster
```py
from redis.cluster import RedisCluster

#r = redis.Redis(host='localhost', port=6379, decode_responses=True)
rc = RedisCluster(host='localhost', port=16379)

print(rc.get_nodes())
# [[host=127.0.0.1,port=16379,name=127.0.0.1:16379,server_type=primary,redis_connection=Redis<ConnectionPool<Connection<host=127.0.0.1,port=16379,db=0>>>], ...

rc.set('foo', 'bar')
# True

rc.get('foo')
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
