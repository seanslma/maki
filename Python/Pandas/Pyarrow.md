# Pyarrow

## data types
https://pandas.pydata.org/docs/user_guide/pyarrow.html

- string[pyarrow]: this is equivalent to pd.StringDtype('pyarrow') that can return NumPy-backed nullable types but slow
- pd.ArrowDtype(pa.string()): will return ArrowDtype much faster
- bool[pyarrow]
- int64[pyarrow]
- uint8[pyarrow]
- uint64[pyarrow]
- float32[pyarrow]
- time64[us][pyarrow]
- timestamp[s][pyarrow]? should use ``

pd.StringDtype('pyarrow'): 
- This allows pandas to utilize PyArrow's memory-efficient string representation for the data
- Additionally, it can return NumPy-backed nullable types, meaning it can handle `missing values` efficiently using NumPy arrays
- string[pyarrow]: This is a shortcut alias for `pd.StringDtype('pyarrow')`

pd.ArrowDtype(pa.string()): 
- It achieves similar memory efficiency as the other options
- it returns ArrowDtype objects instead of NumPy-backed nullable types, soit might be less efficient for handling `missing values` compared to `pd.StringDtype('pyarrow')`

## how to use default pyarrow backend
currently not possible using global setting

```py
data = {'c1': [3, 2, 1, 0], 'c2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame(data)
d2 = df.convert_dtypes(dtype_backend='pyarrow')
d3 = d2.convert_dtypes(dtype_backend='numpy_nullable')
print(df.dtypes)
print(d2.dtypes)
print(d3.dtypes)
```

Notice that 
- df string type is `object` while
- d3 string type is `string[python]`, preserves `pd.NA`
```py
some_series.astype(str)              # object
some_series.astype('string')         # string[python]
some_series.astype(pd.StringDtype()) # string[python]
```

## pyarrow backend issues
- `mod` and `divmod` not implmented: https://github.com/pandas-dev/pandas/pull/56694/files
  ```py
  import pandas as pd
  d = pd.DataFrame({'x': [1,2,3]}, dtype='int64[pyarrow]')
  (d['x'] + 2).mod(2) + 1  
  ```
