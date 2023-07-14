# Parquet

## read `filters`
- The `filters` keyword is a row-group-wise action
- It does not do any filtering within `partitions`
- when using `pyarrow`, the filters will apply to the partition as well
- when do not need all data, it's much fast than using `pd.read_parquet`

## read parquet
Note that if there are no filters, cannot read part of the index levels. See: https://github.com/dask/dask/issues/10386
```py
filters = [
    ('datetime_val', '>=', pd.to_datetime('2023-07-15')),
    (str_val, '==', 'hello'),
    ('int_val', 'in', (1, 2)),
]
schema = pa.schema[
    ('datetime_val', pa.timestamp('ns')),
    ('str_val', pa.string()),
    ('int_val', pa.int64()),
    ('float_val', pa.float64()),
]        
df = dd.read_parquet(
    path=file_path_list,
    filters=filters,
    index=False,
    columns=columns,
    engine='pyarrow',
    storage_options=storage_options,
    open_file_options=dict(precache_options={'method': 'parquet'}),
    schema=schema,
).compute()
```
