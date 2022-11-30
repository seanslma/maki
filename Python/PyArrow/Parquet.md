# Parquet

## compression
```
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
