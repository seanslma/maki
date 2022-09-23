# timeit

## timeit in Jupyter
```
#same line
%timeit -r 3 -n 100 x+y

#one cell
%%timeit -r 3 -n 100
x + y
```

## run timeit in vscode debug
import timeit
```
def func(df):
  df.set_index('a')
  pass

t1 = timeit.Timer(lambda: func(df))
print(t1.timeit(5))
```
