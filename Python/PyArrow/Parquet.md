# Parquet

## df and parquet bytes conversion
```py
import os
import pandas as pd

# df to parquet bytes
df = pd.DataFrame()
df_parquet_bytes = df.to_parquet()
df_parquet_bytes
b'PAR1\x15\x04\x15\x0...'

# parquet bytes to df
parquet_file = io.BytesIO(df_parquet_bytes)
df = pd.read_parquet(parquet_file)
```

## save pa.table to parquet file
```py
import pyarrow as pa
import pyarrow.parquet as pq
table = pa.table({
    'n_legs': [2, 2, 4, 4],
    'animal': ['Flamingo', 'Parrot', 'Dog', 'Horse'],
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
    byts = bio.getbuffer().nbytes
    size.append(byts)
for i, s in enumerate(size):
    print(f'Size: {s / size[0]:.3f}, Time: {tims[i]:.3f}')
```
Output:
```
None   - Size: 1.000, Time:  2.952
snappy - Size: 0.961, Time:  2.961
gzip   - Size: 0.897, Time:  7.333
brotli - Size: 0.601, Time: 10.218
```


