# Lazy Evaludation

## use a class to implement lazy function

## `lazy` package
```
from lazy import lazy
@lazy
def f(x, y):
  v = 0
  for i in range(10000):
    v += x ** y
  return v
  
import time
t0 = time.time()
v = f(12,3)
print(f'time: {time.time() - t0}, value: {v}')
t0 = time.time()
v = f(12,3)
print(f'time: {time.time() - t0}, value: {v}')
```
