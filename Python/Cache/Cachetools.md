# Cachetools

## example
`maxsize`: max number of items in the cache
`ttl`: unit is second
```py
import time
import numpy as np
import pandas as pd
from cachetools import cached, TTLCache

def d1(m, n):
    data = np.random.randn(m, n)
    cols = [f'col{j}' for j in range(1,n+1)]
    df = pd.DataFrame(data, columns=cols)
    return df
    
cache=TTLCache(maxsize=float('inf'),ttl=60)
@cached(cache)
def f1(m,n):
    df=d1(m,n)
    return df
    
t0 = time.time()
d1 = f1(100000,10)
print(f'time: {time.time() - t0:.3f}')
t0 = time.time()
d2 = f1(100000,10)
print(f'time: {time.time() - t0:.3f}')
t0 = time.time()
d3 = f1(100000,10)
print(f'time: {time.time() - t0:.3f}')    
```

## custom key
**caveat**: to ensure thread-safe, we must provide a `Lock` object to the cached decorator.
```py
import threading
from cachetools import cached, TTLCache

CACHE_TIME_LIMIT = 1 * 60 * 60 # one hour
cachetools_cache = TTLCache(maxsize=float('inf'), ttl=CACHE_TIME_LIMIT)

def key_builder(f, namespace, exclude, *args, **kwargs):
    params = {}
    special_type = ''
    for i, v in enumerate(args):
        params[f'arg{i}'] = v
    if isinstance(exclude, str):
        exclude = [exclude]
    for k, v in kwargs.items():
        if exclude is not None and k in exclude:
            continue
        if k == 'special' and isinstance(v, Request):
            special_type = v.headers.get('Accept')
        else:
            if isinstance(v, AzureBlobFileSystem):
                v = {
                    'account_url': v.account_url,
                    'account_name': v.account_name,
                }
            params[k] = v
    return f'{f.__name__}:{namespace}{json.dumps(params)}`{special_type}'

def cachetools_cachedx(f):
    return cached(
        cachetools_cache,
        key=lambda *args, **kwargs: (key_builder(f, *args, **kwargs)),
    )(f)
    
def cachetools_cached(
    namespace: str = '',
    exclude: list[str] = None,
    key_builder: Callable = key_builder,
):
    def decorator(f):
        return cached(
            cachetools_cache,
            key=lambda *args, **kwargs:
                (key_builder(f, namespace, exclude, *args, **kwargs)),
            lock=threading.Lock(), #ensure thread-safe
        )(f)
    return decorator    
    
@cachetools_cached(namespace='dev', exclude='fs', key_builder=key_builder)
def read_parquet_cache(
    *,
    fs: AzureBlobFileSystem,
    path: str,
    columns: list[str],    
) -> pd.DataFrame:
    with fs.open(path) as f:
        df = pd.read_parquet(path=f, columns=columns)
    return df   
```
