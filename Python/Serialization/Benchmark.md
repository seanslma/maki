# Benchmark
parquet has a slower dump speed but is much faster when load back the data and size is much smaller.

## df to bytes to df
average of 5 runs w/o redis
```
   name  dump (redis)  load (redis)    MB
pickle    0.7   (1.9)   1.0   (3.9) 150.5
feather   1.4   (1.8)   0.7   (1.6)  56.7
parquet   2.9   (3.1)   0.9   (1.4)  26.5
```
## pa.Table to bytes to pa.Table
average of 5 runs w/o redis
```
   name  dump (redis)  load (redis)    MB
 pickle   1.1   (2.7)   0.5   (6.0) 269.3
feather   0.5   (0.8)   0.1   (1.2)  56.7
fea(zstd)       (0.8)         (1.0)  42.1
parquet   1.8   (2.1)   0.3   (1.0)  26.5
paq(zstd)       (2.0)         (0.7)  21.0
```

## code
```py
import io
import pickle
from functools import partial
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.feather as pf
import time

test_redis = False

def timeit(func, n=5):
    t0 = time.time()
    for i in range(n):
        func()
    return (time.time() - t0) / n

def pkldumps(d):    
    b = pickle.dumps(d)
    if test_redis:
        r.set('df', b)
    return b

def pklloads(b):
    if test_redis:
        b = r.get('df')    
    return pickle.loads(b)

def paqdumps(d):
    buf = io.BytesIO()
    #pq.write_table(pa.Table.from_pandas(d), buf)       
    pq.write_table(d, buf)      
    b = buf.getvalue()
    if test_redis:
        r.set('df', b)
    return b

def paqloads(b):
    if test_redis:
        b = r.get('df')    
    buf = pa.BufferReader(b)
    #return pq.read_table(buf).to_pandas()  
    return pq.read_table(buf)

def feadumps(d):
    buf = io.BytesIO()
    #d.to_feather(buf)
    pf.write_feather(d, buf)
    b = buf.getvalue()
    if test_redis:
        r.set('df', b)
    return b

def fealoads(b):
    if test_redis:
        b = r.get('df')     
    buf = io.BytesIO(b)
    #return pd.read_feather(buf)
    return pf.read_table(buf)

def hdfdumps(d):
    buf = io.BytesIO()
    d.to_hdf(buf, 'bar', mode='w') #cannot be io stream
    return buf.getvalue()

def hdfloads(b):
    buf = io.BytesIO(b)
    return pd.read_hdf(buf, 'bar', mode='r')

dc = {
    'pickle': [pklloads, pkldumps],
    'feather': [fealoads, feadumps],
    'parquet': [paqloads, paqdumps],
    #'hdf': [hdfloads, hdfdumps],  not supported
}

result = []
for name, (loads, dumps) in dc.items():
    print(name)
    b = dumps(df)
    s = len(b) / 1024 / 1024
    result.append([name, timeit(lambda: dumps(df)), timeit(lambda: loads(b)), s])
dt = pd.DataFrame(result, columns=['name', 'dump', 'load', 'MB'])
print(dt.round(1).to_string(index=False))
```
