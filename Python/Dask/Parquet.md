# Parquet
better to save parquet files without index!!!

## performance
- If read the whole file, `pd.read_parquet` is better.
- If there are row filters `dd.read_parquet` can be faster??? as `pd.read_parquet` need to read the whole index first (how about filters on cols not index???).
- Seems `dd` read multiple parquet files in parallel, but still a little bit slower than parallel `pd`, pd.concat takes lots of time for large files

## read `filters`
- The `filters` keyword is a row-group-wise action
- It does not do any filtering within `partitions`
- when using `pyarrow`, the filters will apply to the partition as well
- when do not need all data, it's much fast than using `pd.read_parquet`? `pd.read_parquet` is about 2-3x faster
- when read without filters, the `dd` requires the loading of all levels of a multi-index df
- for `pd` if use_pandas_metadata, we need to include index columns in the column selection, to be able to restore those in the pandas DataFrame

## read parquet
Note that if there are no filters, cannot read part of the index levels. See: https://github.com/dask/dask/issues/10386
```
Seems this is due to dask still does not fully support multiindex.
A workaround is to read all the index levels and then drop the levels that are not needed.
Another workaround is resetting the index before saving the data to parquet file
- seems it's faster to load data without multiindex and
- we do not need to load all other indexl levels that are not required.
```

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
