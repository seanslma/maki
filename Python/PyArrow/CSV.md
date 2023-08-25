# CSV
pyarrow.csv is much faster than pandas to read csv. see: https://towardsdatascience.com/stop-using-pandas-to-read-write-data-this-alternative-is-7-times-faster-893301633475

## benchmark
```py
import pandas as pd
import pyarrow as pa
import pyarrow.csv as pv

dtype = {
    'name': str,
    'good': bool,
    'value':np.float64,
}
convert_options = pv.ConvertOptions(
    column_types={
        'name': pa.string(),
        'date': pa.timestamp('s'),
        'good': pa.bool_(),
        'value': pa.float64(),
    },
)

d0 = pd.read_csv(f, engine='pyarrow').astype(dtype)              #???
d1 = pd.read_csv(f, dtype=dtype, parse_dates=['date'])           #2.41 s ± 44.3 ms
d2 = pv.read_csv(f).to_pandas().astype(dtype)                    #466 ms ± 125 ms
d3 = pv.read_csv(f, convert_options=convert_options).to_pandas() #276 ms ± 29.7 ms, to pandas
d4 = pv.read_csv(f, convert_options=convert_options)             #175 ms ± 37.1 ms, to pa.Table
```

## example
```py
pyarrow.csv.read_csv(input_file, read_options=None, parse_options=None, convert_options=None, MemoryPool memory_pool=None)
```

## read_options
https://arrow.apache.org/docs/python/generated/pyarrow.csv.ReadOptions.html#pyarrow.csv.ReadOptions
```py
pyarrow.csv.ReadOptions(
    use_threads=None,
    *,
    block_size=None,
    skip_rows=None,
    skip_rows_after_names=None,
    column_names=None,
    autogenerate_column_names=None,
    encoding='utf8',
)
```

## parse_options
https://arrow.apache.org/docs/python/generated/pyarrow.csv.ParseOptions.html#pyarrow.csv.ParseOptions
```py
pyarrow.csv.ParseOptions(
    delimiter=None,
    *,
    quote_char=None,
    double_quote=None,
    escape_char=None,
    newlines_in_values=None,
    ignore_empty_lines=None,
    invalid_row_handler=None,
)
```

## convert_options
https://arrow.apache.org/docs/python/generated/pyarrow.csv.ConvertOptions.html
```py
pyarrow.csv.ConvertOptions(
    check_utf8=None,
    *,
    column_types=None,
    null_values=None,
    true_values=None,
    false_values=None,
    decimal_point=None,
    strings_can_be_null=None,
    quoted_strings_can_be_null=None,
    include_columns=None,
    include_missing_columns=None,
    auto_dict_encode=None,
    auto_dict_max_cardinality=None,
    timestamp_parsers=None,
)

# column types
convert_options = csv.ConvertOptions(
    column_types={"n_legs": pa.float64()},
)

# select columns
convert_options = csv.ConvertOptions(
    include_columns=["animals", "n_legs"],
    include_missing_columns=True,
)

# datetime parser
convert_options = csv.ConvertOptions(
    timestamp_parsers=["%m/%d/%Y", "%m-%d-%Y"],
    auto_dict_encode=True,
)
```
