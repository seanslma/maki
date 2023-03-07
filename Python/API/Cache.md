# Cache

https://aiocache.readthedocs.io/en/latest/caches.html

## question
if there are multiple servers and the next call might not be go to the same server- cache cannot be used!

## Cache StreamingResponse
How to cache StreamReponse or make a cache middleware\
https://github.com/tiangolo/fastapi/issues/4751

Solution: 
- https://github.com/krukov/cashews/issues/107
- cache each chunk of the StreamingResponse content with a separate key
- cache other StreamingResponse properties into a bytes object
- then recreate the StreamingResponse based on the cached content and properties

my solution using aiocache (borrowed code from the following link)
https://github.com/Krukov/cashews/pull/123/files#diff-3df331569a7628a330e72e831d8f338342ef954c7cb3897c6195565a85c32b6fR1
```py
class stream_cached(cached):
    async def set_in_cache(self, key, value):
        try:
            if isinstance(value, StreamingResponse):
                value = await stream_cached.encode_streaming_response(
                    value=value,
                    cache=self.cache,
                    key=key,
                    ttl=self.ttl,
                )
            await self.cache.set(key, value, ttl=self.ttl)
        except Exception:
            cached_logger.exception(
                f"Unexpected error. Couldn't set {value} in key {key}"
            )

    async def get_from_cache(self, key):
        try:
            value = await self.cache.get(key)
            is_streaming_response = (
                value is not None and 'streamingresponse' in key
            )
            if is_streaming_response:
                value = await stream_cached.decode_streaming_response(
                    value=value,
                    cache=self.cache,
                    key=key,
                )
            return value
        except Exception:
            cached_logger.exception(
                f"Unexpected error. Couldn't retrieve key {key}"
            )

    async def encode_streaming_response(
        value: StreamingResponse,
        cache: Cache,
        key: str,
        ttl: object,
    ) -> bytes:
        value.body_iterator = stream_cached.set_iterator(
            cache, key, value.body_iterator, ttl
        )
        serialized_value = b''
        serialized_value += bytes(value.media_type, 'utf-8') + b':'
        serialized_value += bytes(str(value.status_code), 'utf-8') + b':'
        for header_name, header_value in value.raw_headers:
            serialized_value += header_name + b'=' + header_value + b';'
        return serialized_value

    async def decode_streaming_response(
        value: bytes,
        cache: Cache,
        key: str,
    ) -> StreamingResponse:
        media_type, status_code, headers = value.split(b':')
        media_type = str(media_type)
        status_code = int(status_code)
        raw_headers = []
        for header in headers.split(b';'):
            if not header:
                continue
            header_name, header_value = header.split(b'=')
            raw_headers.append((header_name, header_value))
        content = stream_cached.get_iterator(cache, key)
        resp = StreamingResponse(
            content=content,
            media_type=media_type,
            status_code=status_code,
        )
        resp.raw_headers = raw_headers
        return resp

    async def set_iterator(cache: Cache, key: str, iterator, ttl):
        chunk_number = 0
        async for chunk in iterator:
            await cache.set(f'{key}:chunk:{chunk_number}', chunk, ttl=ttl)
            yield chunk
            chunk_number += 1

    async def get_iterator(cache: Cache, key: str):
        chunk_number = 0
        while True:
            chunk = await cache.get(f'{key}:chunk:{chunk_number}')
            if not chunk:
                return
            yield chunk
            chunk_number += 1
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
