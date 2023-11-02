# perf (II)

## ravel() vs flatten()
np.ravel() will avoid copy if possible and thus faster than flatten()

## broadcasting rules
when broadcasting is possible, we do not need to use np.tile()

## numexpr
numexpr is 5x faster than NumPy expression.

```py
a = df['a']
expr = 'sin(a - 1) + 1'
result1 = np.sin(a - 1) + 1
result2 = numexpr.evaluate(expr)
result3 = pd.eval(expr, engine='numexpr')
```

## pd.eval and pd.query
Mainly used for large arrays to save memory thus the speed.

```py
# 2x faster than df1+df2 and less mem
pd.eval('df1 + df2'))

# pd.eval
result1 = (df['A'] + df['B']) / (df['C'] - 1)
result2 = pd.eval("(df.A + df.B) / (df.C - 1)")

# df.eval
result3 = df.eval('(A + B) / (C - 1)')
# add/modify col
df.eval('D = (A + B) / C', inplace=True)

# df.eval with local variable
col_mean = df.mean(1)
result1 = df['A'] + col_mean
result2 = df.eval('A + @col_mean')

# df.query
result1 = df[(df.A < 0.5) & (df.B < 0.5)]
result2 = pd.eval('df[(df.A < 0.5) & (df.B < 0.5)]')
result2 = df.query('A < 0.5 & B < 0.5')

# df.query with local variable
avg = df['C'].mean()
result1 = df[(df.A < avg) & (df.B < avg)]
result2 = df.query('A < @avg & B < @avg')
```
