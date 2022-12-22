# Utils

## list sub packages
```py
import pkgutil
for m in pkgutil.iter_modules(pytoy.__path__, pytoy.__name__ + "."): print(m)
```
