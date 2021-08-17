# Error

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
