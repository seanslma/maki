# Timeit

## timeit in Jupyter
```py
#same line
%timeit -r 3 -n 100 x+y

#one cell
%%timeit -r 3 -n 100
x + y
```

## run timeit in vscode debug
```py
import timeit
def func(df):
  df.set_index('a')
  pass

t1 = timeit.Timer(lambda: func(df))
print(t1.timeit(5))
print(t1.repeat(repeat=3, number=7))
```
