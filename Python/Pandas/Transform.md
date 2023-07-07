# transform

broadcast aggregated value into the group, and function output must be a series.
  * It can produce a scalar value to be broadcast to the shape of the group
  * It can produce an object of the same shape as the input group
  * It must not mutate its input

```py
g = df.groupby('key').value
g.mean()
g.transform('mean')
g.transform(lambda x: x.mean())
g.transform(lambda x: x * 2)
g.transform(lambda x: x.rank(ascending=False))

def normalize(x):
  return (x - x.mean()) / x.std()
g.apply(normalize)
g.transform(normalize)
normalized = (df['value'] - g.transform('mean')) / g.transform('std')
```
