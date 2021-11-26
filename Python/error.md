# Error

## try catch
```python
try:
    run()
except:
    log(f'Error: {sys.exc_info()[0]}. {sys.exc_info()[1]}, line: {sys.exc_info()[2].tb_lineno}')
```

## print trace with except
```python
import traceback

try:
  my_func()
except Exception:
  errmsg = traceback.format_exc()
  print(errmsg)
  return
```
