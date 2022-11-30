# Cache

https://aiocache.readthedocs.io/en/latest/caches.html

## Cache decorator with request header
https://aiocache.readthedocs.io/en/latest/decorators.html

When use cache in api, we should also consider the header. Otherwise different headers will get the same response.
```
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
