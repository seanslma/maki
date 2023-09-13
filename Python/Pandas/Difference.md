# Difference
https://stackoverflow.com/questions/19917545/comparing-two-pandas-dataframes-for-differences

## df.equals
Return a bool. not very reliable regarding floats

## df.compare
Return a dataframe. same shape and type. not reliable either

if all are numbers, using `np.allclose`
```py
np.allclose(df1, df2, rtol=1e-6, atol=1e-6)
```
