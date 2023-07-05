# Parquet

## perf benchmark
best is
- to bytes: `pq.write_table(pa.Table.from_pandas(df), buf)`
- from bytes: pq.read_table(pa.BufferReader(bytes)).to_pandas()`
```py
def paqdumps(d, i):
    buf = io.BytesIO()
    if i==0:
        # 3.15 s ± 88.8 ms
        d.to_parquet(buf)
    else:
        # 3.09 s ± 126 ms
        table = pa.Table.from_pandas(d)
        pq.write_table(table, buf)       
    return buf.getvalue()

def paqloads(b, i):    
    if i==0:
        # 1.79 s ± 18.9 ms
        buf = io.BytesIO(b)
        f = pd.read_parquet(buf)
    elif i==1:    
        # 1.75 s ± 20.3 ms
        buf = pa.BufferReader(b)
        f = pd.read_parquet(buf)      
    elif i==2:
        # 1.83 s ± 15.5 ms, to_pandas is slow
        buf = io.BytesIO(b)
        f = pq.read_pandas(buf).to_pandas()
    elif i==3: 
        # 1.72 s ± 27.2 ms
        buf = pa.BufferReader(b)
        f = pq.read_pandas(buf).to_pandas()  
    elif i==4:
        # 1.77 s ± 72.9 ms
        buf = io.BytesIO(b)
        f = pq.read_table(buf).to_pandas()
    elif i==5: 
        # 1.70 s ± 21.8 ms
        buf = pa.BufferReader(b)
        f = pq.read_table(buf).to_pandas()         
    return f

for i in range(2):
    t0 = time.time()
    b = paqdumps(d, i)
    print(f'dump {i}: {time.time() - t0:.3f}')
for i in range(6):
    t0 = time.time()
    f = paqloads(b, i)
    print(f'load {i}: {time.time() - t0:.3f}')  
```
