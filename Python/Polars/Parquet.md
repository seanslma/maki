# Parquet

## read parquet with filters
https://github.com/pola-rs/polars/issues/3964
- generate random df
- read parquet using duckdb
- read parquet using polars - cannot use string datetime (polars will cast column to string) - have to use datetime

performance benchmark (parquet with index 8 MB)
```
    all    filters + columns
pl: 0.7ms  337ms
pd: 1.01s  479ms
dk: 2.00s  591ms (nrow incorrect)
```

performance benchmark (parquet without index 8 MB)
```
    all    filters + columns
pl: 0.7ms  337ms
pd: 1.01s  479ms
dk: 

polars
```py
import polars as pl
from datetime import datetime

df = (
    pl
    .scan_parquet('df.parquet')
    .filter(pl.col('dt') >= datetime(2020,4,1))
    .filter(pl.col('val').is_not_null())
    .select(['c1', 'c2', 'c4'])
).collect().to_pandas()

print(df.shape)
```

duckdb
```py
import duckdb

query = """
select
    c1, c2, c4
from
    read_parquet('df.parquet')
where
    dt >= '2020-04-01'
    and val is not null
"""
df = duckdb.query(query).to_df()

print(df.shape)
```
