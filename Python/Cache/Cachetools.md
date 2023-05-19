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
