# Parquet

## Read parquet with filters
https://github.com/pola-rs/polars/issues/3964
- generate random df
- read parquet using duckdb
- read parquet using polars - cannot use string datetime (polars will cast column to string) - have to use datetime

**Performance benchmark** (parquet with index 8 MB)
```
    all    filters + columns
pl: 0.70s  337ms
pd: 1.01s  479ms
dk: 2.00s  591ms
```

**Performance benchmark** (parquet without index 40 MB)
- file size is similar to without category
- best to save parquet file with **category** and read it with pandas.
```
    String                                                 Category
    all    filter_string + columns  filter_date + columns  all    filter_category + columns  filter_date + columns
pl: 3.21s  445ms                    758ms                  914ms  349ms                      552ms
pd: 3.33s  941ms                    1.10s                  684ms  299ms                      306ms
dk: 5.57s  597ms                    1.01s                  5.56s  536ms                      983ms
```

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
