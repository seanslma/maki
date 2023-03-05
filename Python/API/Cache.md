# Cache

https://aiocache.readthedocs.io/en/latest/caches.html

## Cache StreamingResponse
How to cache StreamReponse or make a cache middleware\
https://github.com/tiangolo/fastapi/issues/4751

Solution: https://github.com/krukov/cashews/issues/107

my solution using aiocache
```py
```

## key_builder
```py
def key_builder(f, **kwargs):
    return f.__name__ + json.dumps({
        k: v for k, v in kwargs.items() if k != 'request'
    })
```

## Cache decorator with request header
https://aiocache.readthedocs.io/en/latest/decorators.html

When use cache in api, we should also consider the header. Otherwise different headers will get the same response.

**Issue**: StreamingResponse is not supported as data is sent chunk by chunk - only the last chunk (empty string) is cached. See `StreamingResponse` definition.
```py
from typing import Optional
from aiocache import cached, Cache
from fastapi import status, Request, Header

@router.get(
    "/hello",
    status_code=status.HTTP_200_OK,
    description='Get hello'
)
@vary_on_headers('Accept')
@cached(ttl=3600, cache=Cache.MEMORY, namespace='dev', key_builder=key_builder)
async def get_hello(
    request: Request,
    accept: Optional[str] = Header(None), # header is `Accept`
):
    return 'hello, Accept header is `{accept}`'
```

## Cache dataframe
https://github.com/aio-libs/aiocache/issues/493
```py
import zlib
import pickle
import pandas as pd

import asyncio
from aiocache import Cache
from aiocache.serializers import BaseSerializer

class CompressionSerializer(BaseSerializer):
    DEFAULT_ENCODING = None #zlib works with bytes

    def dumps(self, value):
        compressed = zlib.compress(pickle.dumps(value))
        return compressed

    def loads(self, value):
        #if value is too large to read into memory
        #use zlib.decompressobj instead of zlib.decompress 
        decompressed = pickle.loads(zlib.decompress(value))
        return decompressed

cache = Cache(Cache.MEMORY, serializer=CompressionSerializer(), namespace='dev')

df = pd.DataFrame({'x':[1,2], 'y':[3,4]})
loop = asyncio.get_event_loop()
loop.run_until_complete(cache.set("key", df))
loop.run_until_complete(cache.get("key"))
loop.run_until_complete(cache.delete("key"))
```
