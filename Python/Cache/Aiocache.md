# Aiocache
Asyncio cache supporting multiple backends (memory, redis and memcached).

Aiocache is an asynchronous caching library that is based on asyncio. 
This means that it can be used to cache data in an asynchronous way, 
which can be useful for improving the performance of I/O-bound applications.

## cached
Do not use `aiocache.cached` for a sync function. It will return a coroutine object.

## config
```py
from aiocache import caches, Cache
caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache",
        'serializer': {
            'class': "aiocache.serializers.StringSerializer"
        }
    },
    'redis': {
        'cache': "aiocache.RedisCache",
        'endpoint': "127.0.0.10",
        'port': 6378,
        'serializer': {
            'class': "aiocache.serializers.PickleSerializer"
        }
    }
})
cache = Cache(Cache.REDIS, endpoint="127.0.0.10", port=6379)
```

## how to use redis to cache StreamingResponse
