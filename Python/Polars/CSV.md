# CSV benchmark

## read csv (150 MB) with categorical/string
For csv file reading, the fastest method is using `pv.read_csv(file, convert_options).to_pandas()`.
```py
# Method                                                          Categorical    String   Format
pv.read_csv(file, convert_options=pa_convert_options)             #0.42s         0.32s    pa.Table
pv.read_csv(file, convert_options=pa_convert_options).to_pandas() #0.48s         0.75s    pd.DataFrame
pl.read_csv(file, dtypes=pl_dtypes).to_pandas()                   #2.82s         2.01s    pd.DataFrame
pv.read_csv(file).to_pandas().astype(pd_dtypes)                   #3.20s         2.09s    pd.DataFrame
pd.read_csv(file, dtype=pd_dtype, parse_dates=['date'])           #16.2s         15.3s    pd.DataFrame
```

```py
import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.csv as pv

pd_categorical = 'category' #'string'
pd_dtype = {
    'country': pd_categorical,
    'val': 'Float64',
}
pd_dtypes = pd_dtype.copy()
pd_dtypes['date'] = 'datetime64[ns]'

pl_categorical = pl.Categorical # pl.String
pl_dtypes = {
    'date': pl.Date, 
    'country': pl_categorical, 
    'val': pl.Float64, 
}

# pa_categorical = pa.string()
pa_categorical = pa.dictionary(pa.int32(), pa.string()) # CSV conversion to dictionary only supported for int32 indices
pa_convert_options = pv.ConvertOptions(
    column_types={
        'date': pa.timestamp('ns'),
        'country': pa_categorical,
        'val': pa.float64(),      
    }
) 
```
