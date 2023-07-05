# Benchmark

## df to bytes to df
average of 5 runs
```
     name  dump  load    MB
   pickle   0.7   1.0 150.5
pickle-p2   1.3   1.4 173.2
  feather   1.4   0.7  56.7
  parquet   2.9   0.9  26.5
```

code
```py
import io
import pickle
from functools import partial
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import time

def timeit(func, n=5):
    t0 = time.time()
    for i in range(n):
        func()
    return (time.time() - t0) / n

def paqdumps(d):
    buf = io.BytesIO()
    pq.write_table(pa.Table.from_pandas(d), buf)       
    return buf.getvalue()

def paqloads(b):
    buf = pa.BufferReader(b)
    return pq.read_table(buf).to_pandas()  

def feadumps(d):
    buf = io.BytesIO()
    d.to_feather(buf)
    return buf.getvalue()

def fealoads(b):
    buf = io.BytesIO(b)
    return pd.read_feather(buf)

def hdfdumps(d):
    buf = io.BytesIO()
    d.to_hdf(buf, 'bar', mode='w') #cannot be io stream
    return buf.getvalue()

def hdfloads(b):
    buf = io.BytesIO(b)
    return pd.read_hdf(buf, 'bar', mode='r')

dc = {
    'pickle': [pickle.loads, pickle.dumps],
    'pickle-p2': [pickle.loads, partial(pickle.dumps, protocol=2)], 
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
print(dt.to_string(index=False))
```
