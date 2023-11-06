# stats

## round
The round() function rounds values of .5 towards an even integer (Python Docs, n.d. a). So .5 is round up for positive values and round down for negative values.

For instance, both round(0.5) and round(-0.5) return 0, while round(1.5) gives 2 and round(-1.5) gives -2. This Python behaviour is a bit different from how rounding usually goes.

## pd.quantile
#1, consider the first and last values are the edges:
```
h = (N − 1)*p + 1 #space is between v1 and vn
Est_Quantile = x⌊h⌋ + (h − ⌊h⌋)*(x⌊h⌋ + 1 − x⌊h⌋)
```

not #2, consider the first and last values are the first and last data centers:
```
h = N*p + 0.5
Est_Quantile = x⌊h⌋ + (h − ⌊h⌋)*(x⌊h⌋ + 1 − x⌊h⌋)
```
