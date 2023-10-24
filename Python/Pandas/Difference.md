# Difference
https://stackoverflow.com/questions/19917545/comparing-two-pandas-dataframes-for-differences

## df.equals
Will check both dtypes and data.
Return a bool. not very reliable regarding floats

## df.compare
Will only check data.
Return a dataframe. same shape and type. not reliable either (we need to consider rounding errors)
```py
df.compare(dp).empty #return True if same

# workaround - define a round function
def round_df(df, decimal=6):
    tmp = df.select_dtypes(include=[np.number])
    df.loc[:, tmp.columns] = np.round(tmp)
    return df
```

if all are numbers, using `np.allclose`
```py
np.allclose(df1, df2, rtol=1e-6, atol=1e-6)
```
