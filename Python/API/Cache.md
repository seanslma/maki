# Cache

https://aiocache.readthedocs.io/en/latest/caches.html

## Cache decorator
https://aiocache.readthedocs.io/en/latest/decorators.html

When use cache in api, we should also consider the header. Otherwise different headers will get the same response.
```
from aiocache import cached, Cache
from django.views.decorators.vary import vary_on_headers

@router.get(
    "/hello",
    status_code=status.HTTP_200_OK,
    description='Get hello'
)
@vary_on_headers('Accept')
@cached(ttl=3600, cache=Cache.MEMORY, namespace='dev', key_builder=key_builder)
async def get_hello(
    request: Request,
):
    return 'hello'
```
