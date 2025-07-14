# Stream

https://docs.python.org/3/library/io.html

## parquet cache
When reading a parquet from a fastapi using `pd.read_parquet`, if it's stream and has cache, we might get the error like `pyarrow.lib.ArrowInvalid: Could not open Parquet input source '<Buffer>': Parquet magic bytes not found in footer. Either the file is corrupted or this is not a parquet file.`

Because there is too much data???
