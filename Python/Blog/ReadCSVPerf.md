# Reading CSV Files: the Fast, Faster and Fastest Options

CSV (comma-separated values) files have been widely used in different areas. They can be easily exported from almost all programming languages. They can also be loaded into all text editors and many other applications. However, the main disadvantage is that CSV files are usually larger than files with other formats and it is slow to load them into memory.

Here we compare different options for reading CSV files by using the `pandas`, `polars` and `pyarrow` Python packages. We test the loading performance for CSV files each with a different data type. Based on the test results, we should be able to determine which option to use when we need reading CSV files faster.

## Creating test data
CSV files with three data types, `string`, `float`, and `datetime`, have been used to test the file reading performance. All the testing CSV files were created using the scripts in <a href="https://medium.com/@sean.lma/how-to-create-dummy-pandas-dataframes-for-testing-cf03c52878e3">my previous post</a>; each CSV file has 10 million rows and three columns with the same data type.

The `string` type CSV file was created with:
```py
df_str = gen_rand_df(
    nrow=10000000,
    str_cols={
        'count': 3,
        'name': ['c1', 'c2', 'c3'],
        'str_len': [10, (1,15), (1,50)],
        'str_count': [1000, 500, 100],
    },
)
df_str.to_csv(filename, index=False)
```

The `float` type CSV file was created with:
```py
df_flt = gen_rand_df(
    nrow=10000000,
    float_cols={
        'count': 3,
        'name': ['c1', 'c2', 'c3'],
        'low': [0, -100, 0],
        'high': [1, 100, 1e5],
    },
)
df_flt.to_csv(filename, index=False)
```

The `datetime` type CSV file was created with:
```py
df_dts = gen_rand_df(
    nrow=10000000,
    ts_cols={
        'count': 3,
        'name': ['c1', 'c2', 'c3'],
        'start_date': ['2020-01-01', '2021-01-01', '2022-01-01'],
        'end_date': ['2021-01-01', '2022-01-01', '2023-01-01'],
        'freq': 's',
        'random': False,
    },
)
df_dts.to_csv(filename, index=False)
```

## Reading CSV files using `pandas`
In pandas, when reading CSV files, there are three available parsers (`python`, `c`, and `pyarrow`). The parser can be set via the parameter `engine`. 

and two backend data types (backend_dtype: `numpy_nullable` and `pyarrow`) for storing the data.
# str
pd_dtype_s = {
    'c1': str,
    'c2': str,
    'c3': str,
}
# pd.ArrowDtype(pa.string()) will return ArrowDtype
pd_dtype_pa_s = {
    'c1': pd.ArrowDtype(pa.string()),
    'c2': pd.ArrowDtype(pa.string()),
    'c3': pd.ArrowDtype(pa.string()),
}
# pd.StringDtype('pyarrow') can return NumPy-backed nullable types
pd_dtype_pa_s2 = {
    'c1': 'string[pyarrow]',
    'c2': 'string[pyarrow]',
    'c3': 'string[pyarrow]',
}

pd_dtype_f = {
    'c1': float,
    'c2': float,
    'c3': float,
}
pd_dtype_f_pa = {
    'c1': 'float64[pyarrow]',
    'c2': 'float64[pyarrow]',
    'c3': 'float64[pyarrow]',
}

pd_dtype_t = {
    'c1': 'datetime64[ns]',
    'c2': 'datetime64[ns]',
    'c3': 'datetime64[ns]',
}
pd_dtype_t_pa = {
    'c1': pd.ArrowDtype(pa.timestamp('ns')),
    'c2': pd.ArrowDtype(pa.timestamp('ns')),
    'c3': pd.ArrowDtype(pa.timestamp('ns')),
}

## Reading CSV files using `polars`

## Reading CSV files using `pyarrow`

## Best options from `pandas`, `polars`, and `pyarrow`


```py

# %%
import duckdb
import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.csv as pv
from mapy.test import gen_rand_df


pa_dtype_s = {
    'c1': pa.string(),
    'c2': pa.string(),
    'c3': pa.string(),
}
pl_dtype_s = {
    'c1': pl.Utf8,
    'c2': pl.Utf8,
    'c3': pl.Utf8,
}
convert_options_s = pv.ConvertOptions(
    column_types=pa_dtype_s,
)
# float

pa_dtype_f = {
    'c1': pa.float64(),
    'c2': pa.float64(),
    'c3': pa.float64(),
}
pl_dtype_f = {
    'c1': pl.Float64,
    'c2': pl.Float64,
    'c3': pl.Float64,
}
convert_options_f = pv.ConvertOptions(
    column_types=pa_dtype_f,
)
# datetime

pa_dtype_t = {
    'c1': pa.timestamp('ns'),
    'c2': pa.timestamp('ns'),
    'c3': pa.timestamp('ns'),
}
pl_dtype_t = {
    'c1': pl.Datetime,
    'c2': pl.Datetime,
    'c3': pl.Datetime,
}
convert_options_t = pv.ConvertOptions(
    column_types=pa_dtype_t,
)


col_type = 'dts' # str, flt, dts
file_dir = '/home/sma/dat'
file = f'{file_dir}/df_{col_type}.csv'

# %%
# str
if col_type == 'str':
    pd_dtype = pd_dtype_s
    pd_dtype_pa = pd_dtype_pa_s
    pa_dtype = pa_dtype_s
    pl_dtype = pl_dtype_s
    convert_options = convert_options_s

# %%
# float
if col_type == 'flt':
    pd_dtype = pd_dtype_f
    pd_dtype_pa = pd_dtype_f_pa
    pa_dtype = pa_dtype_f
    pl_dtype = pl_dtype_f
    convert_options = convert_options_f

# %%
# datetime
if col_type == 'dts':
    pd_dtype = pd_dtype_t
    pd_dtype_pa = pd_dtype_t_pa
    pa_dtype = pa_dtype_t
    pl_dtype = pl_dtype_t
    convert_options = convert_options_t

# %%
# data = {'c1': [3, 2, 1, 0], 'c2': ['a', 'b', 'c', 'd']}
# df = pd.DataFrame(
#     data,
#     dtype={'c1':'int64[pyarrow]', 'c2':'string[pyarrow]'},
# )
# d2 = df.convert_dtypes(dtype_backend='pyarrow')
# d3 = d2.convert_dtypes(dtype_backend='numpy_nullable')
# print(df.dtypes)
# print(d2.dtypes)
# print(d3.dtypes)

# %% [markdown]
# ## pandas

# %%
_ = """
physical_cores: 4  pandas: 2.2.2         pyarrow: 16.0.0          pyarrow: 16.0.0
logical_cores : 4                        logical_cores : 8        polars : 0.20.25
                                                         str    float  datetime   str    float  datetime
c       + numpy_nullable + astype                        3.93s  18.2s  18.5s      12.7s  56.5s  106.s
c       + numpy_nullable + dtype                         3.88s  3.29s  15.4s      11.7s  12.4s  91.0s
c       + pyarrow        + dtype                         3.27s  3.55s  16.6s      12.4s  12.2s  -
c       + pyarrow        + dtype_pa                      5.17s  16.8s  53.2s      21.4s  54.4s  193.s
pyarrow + numpy_nullable + dtype                         3.50s  0.54s  1.15s      15.5s  1.83s  23.6s
pyarrow + pyarrow        + dtype                         7.62s  0.50s  1.67s      31.5s  2.05s  6.94s
pyarrow + pyarrow        + string[pyarrow]               4.05s  15.8s  11.1s      14.3s  57.6s  49.7s
pyarrow + pyarrow        + dtype_pa                      0.39s  0.48s  0.44s      1.41s  1.21s  1.42s
pyarrow + pyarrow        + dtype_pa + to numpy_nullable  2.74s  2.68s  1.64s      12.1s  8.90s  5.74s
pyarrow + pyarrow                                        0.48s  0.47s  0.37s      1.39s  1.53s  1.21s
"""

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(
    file, dtype=pd_dtype_s, engine='c', dtype_backend='numpy_nullable'
).astype(pd_dtype)

# %%
%%timeit -r 3 -n 7
if col_type == 'dts':
    d = pd.read_csv(
        file, engine='c', dtype_backend='numpy_nullable', parse_dates=['c1', 'c2', 'c3'], date_format='%Y-%m-%d %H:%M:%S'
    )
else:
    d = pd.read_csv(file, engine='c', dtype_backend='numpy_nullable', dtype=pd_dtype)

# %%
%%time
#it -r 3 -n 7
if col_type == 'dts':
    d = pd.read_csv(file, engine='c', dtype_backend='pyarrow',  parse_dates=['c1', 'c2', 'c3'], date_format='%Y-%m-%d %H:%M:%S')
else:
    d = pd.read_csv(file, engine='c', dtype_backend='pyarrow', dtype=pd_dtype)

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(file, engine='c', dtype_backend='pyarrow', dtype=pd_dtype_pa)

# %%
%%timeit -r 3 -n 7
if col_type == 'dts':
    d = pd.read_csv(
        file, engine='pyarrow', dtype_backend='numpy_nullable', parse_dates=['c1', 'c2', 'c3'], date_format='%Y-%m-%d %H:%M:%S'
    )
else:
    d = pd.read_csv(file, engine='pyarrow', dtype_backend='numpy_nullable', dtype=pd_dtype)

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype)

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype_pa_s2)

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype_pa)

# %%
if col_type == 'dts':
    pd_dtype_pa = {
        'c1': 'datetime64[us]',
        'c2': 'datetime64[us]',
        'c3': 'datetime64[us]',
    }#KeyError: TimestampType(timestamp[ns]) timestamp[ns] cannot be converted to datetime64[ns]

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype_pa).convert_dtypes(dtype_backend='numpy_nullable')

# %%
# %%timeit -r 3 -n 7
# d = pd.read_csv(
#     file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype_s_pa
# ).astype(pd_dtype_pa)

# %%
# %%timeit -r 3 -n 7
# if col_type == 'str':
#     pass
# elif col_type == 'dts':
#     d = pd.read_csv(
#         file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype_s_pa
#     ).assign(
#         c1=lambda x: pd.to_datetime(x['c1'], format='%Y-%m-%d %H:%M:%S'),
#         c2=lambda x: pd.to_datetime(x['c2'], format='%Y-%m-%d %H:%M:%S'),
#         c3=lambda x: pd.to_datetime(x['c3'], format='%Y-%m-%d %H:%M:%S'),
#     )
# elif col_type == 'flt':
#     d = pd.read_csv(
#         file, engine='pyarrow', dtype_backend='pyarrow', dtype=pd_dtype_s_pa
#     ).assign(
#         c1=lambda x: pd.to_numeric(x['c1'], errors='coerce'),
#         c2=lambda x: pd.to_numeric(x['c2'], errors='coerce'),
#         c3=lambda x: pd.to_numeric(x['c3'], errors='coerce'),
#     )

# %%
%%timeit -r 3 -n 7
d = pd.read_csv(file, engine='pyarrow', dtype_backend='pyarrow')

# %% [markdown]
# # polars

# %%
_ = """
physical_cores: 4  pandas: 2.2.2         pyarrow: 16.0.0          pyarrow: 16.0.0
logical_cores : 4                        logical_cores : 8        polars : 0.20.25

                                          str    float  datetime   str    float  datetime
default                                   0.52s  0.38s  0.37s      1.89s  1.23s  1.08s
eager                                     0.46s  0.40s  0.39s      1.60s  0.93s  1.61s
lazy                                      0.45s  0.38s  0.41s      1.75s  1.12s  1.56s
streaming                                 0.42s  0.40s  0.42s      1.50s  1.06s  1.66s
sql api eager                             0.46s  0.38s  0.40s      1.63s  1.05s  1.57s
sql api eager + to pandas numpy_nullable  1.59s  0.47s  0.48s      5.94s  1.29s  1.74s
sql api eager + to pandas pyarrow         0.99s  0.43s  0.45s      3.36s  1.10s  1.71s
"""

# %%
%%timeit -r 3 -n 7
# default
d = pl.read_csv(file)

# %%
%%timeit -r 3 -n 7
# eager
d = pl.read_csv(file, dtypes=pl_dtype)

# %%
%%timeit -r 3 -n 7
# lazy
d = pl.scan_csv(file, dtypes=pl_dtype).collect()

# %%
%%timeit -r 3 -n 7
# streaming
d = pl.scan_csv(file, dtypes=pl_dtype).collect(streaming=True)

# %%
%%timeit -r 3 -n 7
# read csv with sql api
d = pl.SQLContext(data=pl.scan_csv(file, dtypes=pl_dtype)).execute('select * from data', eager=True)

# %%
%%timeit -r 3 -n 7
# read csv with sql api and to pandas df
d = pl.SQLContext(data=pl.scan_csv(file, dtypes=pl_dtype)).execute('select * from data', eager=True).to_pandas(use_pyarrow_extension_array=False)

# %%
%%timeit -r 3 -n 7
# read csv with sql api and to pandas df
d = pl.SQLContext(data=pl.scan_csv(file, dtypes=pl_dtype)).execute('select * from data', eager=True).to_pandas(use_pyarrow_extension_array=True)

# %% [markdown]
# # duckdb

# %%
_ = """
physical_cores: 4  pandas: 2.2.2         pyarrow: 16.0.0          pyarrow: 16.0.0          pyarrow: 11.0.0
logical_cores : 4                        logical_cores : 8        polars : 0.20.25         polars : 0.20.13
                                         str    float  datetime   str    float  datetime   str    float  datetime
default                                  6.31s  3.27s  4.86s      25.1s  17.3s  19.0s      30.5s  10.7s  15.4s
default to pandas                        2.91s  1.32s  1.50s      18.8s  5.07s  5.73s      16.2s  3.56s  6.06s
"""

# %%
%%time
# duckdb
d = duckdb.sql(f'select * from read_csv_auto("{file}")').fetchall()

# %%
%%time
# convert to pandas df
d = duckdb.sql(f'select * from read_csv_auto("{file}")').df()

# %% [markdown]
# # pyarrow

# %%
_ = """
physical_cores: 4  pandas: 2.2.2       pyarrow: 16.0.0          pyarrow: 16.0.0          pyarrow: 11.0.0
logical_cores : 4                      logical_cores : 8        polars : 0.20.25         polars : 0.20.13
                                    str    float  datetime   str    float  datetime   str    float  datetime
default                             0.39s  0.44s  0.38s      1.23s  1.26s  1.11s      1.08s  1.05s  1.61s
default + to pandas numpy_nullable  1.07s  0.45s  0.42s      3.64s  1.37s  1.16s      3.37s  1.19s  1.41s
default + to pandas pyarrow         0.48s  0.43s  0.33s      3.92s  1.57s  5.67s      4.14s  1.39s  1.56s
dtype                               0.39s  0.40s  0.36s      1.00s  1.16s  1.06s      0.93s  1.03s  1.14s
dtype   + to pandas numpy_nullable  0.99s  0.45s  0.41s      3.41s  1.61s  1.11s      3.27s  1.15s  1.16s
dtype   + to pandas pyarrow         0.39s  0.42s  0.37s      1.02s  1.51s  1.06s      0.94s  1.02s  1.11s
"""

# %%
%%timeit -r 3 -n 7
d = pv.read_csv(file)

# %%
%%timeit -r 3 -n 7
d = pv.read_csv(file).to_pandas()

# %%
%%timeit -r 3 -n 7
d = pv.read_csv(file).to_pandas(types_mapper=pd.ArrowDtype)

# %%
%%timeit -r 3 -n 7
d = pv.read_csv(file, convert_options=convert_options)

# %%
%%timeit -r 3 -n 7
# df = pa.table(dict_of_numpy_arrays).to_pandas(use_threads=False) # default multi-thread
d = pv.read_csv(file, convert_options=convert_options).to_pandas()

# %%
%%timeit -r 3 -n 7
d = pv.read_csv(file, convert_options=convert_options).to_pandas(types_mapper=pd.ArrowDtype)

# %%
import platform
import psutil
import multiprocessing

cpu_type = platform.processor()
physical_cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)

# include "virtual" hyperthreaded cpus
num_physical_cores = multiprocessing.cpu_count()

print(f'cpu_type      : {cpu_type}')
print(f'physical_cores: {physical_cores}')
print(f'logical_cores : {logical_cores}')
print(f'num_of_cores  : {num_physical_cores}')

```
