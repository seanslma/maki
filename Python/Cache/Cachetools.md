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
```py
from cachetools import cached, TTLCache

CACHE_TIME_LIMIT = 1 * 60 * 60 # one hour
cachetools_cache = TTLCache(maxsize=float('inf'), ttl=CACHE_TIME_LIMIT)

def key_builder(f, *args, **kwargs):
    params = {}
    special_type = ''
    for i, v in enumerate(args):
        params[f'arg{i}'] = v
    for k, v in kwargs.items():
        if k == 'special' and isinstance(v, Request):
            special_type = v.headers.get('Accept')
        else:
            if isinstance(v, AzureBlobFileSystem):
                v = {
                    'account_url': v.account_url,
                    'account_name': v.account_name,
                }
            params[k] = v
    return f.__name__ + json.dumps(params) + f'`{special_type}'

def cachetools_cached(f):
    return cached(
        cachetools_cache,
        key=lambda *args, **kwargs: (key_builder(f, **kwargs)),
    )(f)
    
@cachetools_cached
def read_parquet_cache(
    namespace: str,
    *,
    fs: AzureBlobFileSystem,
    path: str,
    columns: list[str],    
) -> pd.DataFrame:
    with fs.open(path) as f:
        df = pd.read_parquet(path=f, columns=columns)
    return df   
```
