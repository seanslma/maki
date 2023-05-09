# Parquet

## save pa.table to parquet file
```py
import pyarrow as pa
table = pa.table({
    'n_legs': [2, 2, 4, 4],
    'animal': ['Flamingo', 'Parrot', 'Dog', 'Horse],
})

# directly write to file
pq.write_table(table=table, where='data.parquet', compression='zstd')

# write to buffer first
buf = pa.BufferOutputStream()
pq.write_table(table=table, where=buf, compression='zstd')

blob = buf.getvalue()
buf = pa.py_buffer(blob)
with fs.open('data.parquet', mode='wb') as f:
    f.write(buf)
```

## compression
```py
size = []
tims = []
import time
df = pd.read_parquet('test.parquet').reset_index()
for c in [None, 'snappy', 'gzip', 'brotli']:
    t0 = time.time()
    bio = io.BytesIO(df.to_parquet(compression = c))
    tims.append(time.time() - t0)
    byt = bio.getbuffer().nbytes
    size.append(byt)
for i, s in enumerate(size):
    print(f'{s / size[0]:.3f} TIME: {tims[i]:.3f}')
```
Out put:
```
1.000 TIME:  2.952
0.961 TIME:  2.961
0.897 TIME:  7.333
0.601 TIME: 10.218
```
