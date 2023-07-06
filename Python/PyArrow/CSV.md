# CSV
pyarrow.csv is much faster than pandas to read csv. see: https://towardsdatascience.com/stop-using-pandas-to-read-write-data-this-alternative-is-7-times-faster-893301633475

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
