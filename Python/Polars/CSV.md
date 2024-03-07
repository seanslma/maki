# CSV benchmark

## read csv (150 MB) with categorical
```py
import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.csv as pv

pd_categorical = 'category'
pd_dtype = {
    'country': pd_categorical,
    'val': 'Float64',
}
pd_dtypes = pd_dtype.copy()
pd_dtypes['date'] = 'datetime64[ns]'

pl_dtypes = {
    'date': pl.Date, 
    'country': pl.Categorical, 
    'val': pl.Float64, 
}

pa_categorical = pa.dictionary(pa.int32(), pa.string()) # CSV conversion to dictionary only supported for int32 indices
pa_convert_options = pv.ConvertOptions(
    column_types={
        'date': pa.timestamp('ns'),
        'country': pa_categorical,
        'val': pa.float64(),      
    }
) 

pv.read_csv(file, convert_options=pa_convert_options)             #0.74s, to pa.Table
pv.read_csv(file, convert_options=pa_convert_options).to_pandas() #0.49s, to pandas
pl.read_csv(file, dtypes=pl_dtypes).to_pandas()                   #1.27s
pv.read_csv(file).to_pandas().astype(pd_dtypes)                   #3.20s
pd.read_csv(file, dtype=pd_dtype, parse_dates=['date'])           #18.5s
```

## read csv (150 MB) with string
