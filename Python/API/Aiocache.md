# Aiocache

## config
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

## how to use redis to cache StreamingResponse
