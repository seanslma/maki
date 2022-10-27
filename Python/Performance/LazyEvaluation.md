# Lazy Evaludation

## use a class to implement lazy function
```
class Test():
    def __init__(self, name):
        self.name = name
        self._value = None
        
    @property
    def value(self):
        if self._value is None:
            self._value = self._get_value()
        return self._value

    def _get_value(self):
        val = my_api(self.name)
        return val
```

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
