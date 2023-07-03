# DataFrame

## MultiIndex
cavaet: **NotImplementedError**: *Dask dataframe does not yet support multi-indexes*. At least not fully supported.

- If multiindex is not required, save the dataframe as a parquet file by resetting the index. 
- It's much faster to load a parquet file without multiindex, though the total time including recreating the index is a little longer.
- Aslo, we can read any level separately much faster - with multiindex, we need to read all the index levels together. 

Example
```py
%%timeit -r 3 -n 3
files = ['/tmp/data.parquet']
# directly load all index levels
di = dd.read_parquet(
    files,
    index=None,
    columns=['val1', 'val2'],
    engine='pyarrow',
    open_file_options=dict(precache_options=dict(method='parquet')),
).groupby(['idx2']).sum().compute()
# load all index levels as cols
di = dd.read_parquet(
    files,
    index=False,
    columns=['idx1', 'idx2', 'idxn', 'val1', 'val2'],
    engine='pyarrow',
    open_file_options=dict(precache_options=dict(method='parquet')),
).drop(columns=['idx1', 'idxn']).groupby(['idx2']).sum().compute()
```

## Partition
