# timeit

## run timeit in vscode debug

```
def f1(df):
  df.set_index('a')
  pass
t1 = timeit.Timer(lambda: f1(df))

print(t1.timeit(5))
```
