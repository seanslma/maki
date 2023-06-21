# Error

## try catch
```python
try:
    run()
except Exception as exc:
    log(f'Error: {sys.exc_info()[0]}. {sys.exc_info()[1]}, line: {sys.exc_info()[2].tb_lineno}')
finally:
    ok = 1 #do anything else
```

## print trace with except
```python
import traceback

try:
  my_func()
except Exception as exc:
  errmsg = traceback.format_exc()
  print(errmsg)
  return
```

## use `warnings` module to elevate warnings to errors
```
warnings.simplefilter('error', FutureWarning)
```
