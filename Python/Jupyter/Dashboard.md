# Dashboard

## Output logging info from dashboard

### Simple and effective
```py
import traceback
def to_log(msg)
    with open("err.log", "a") as f:
        f.write(f'{msg}\n\n')

try:
    x = 1 / 0
except Exception as exec:
    to_log(traceback.format_exc())
    pass
```

### widgets.Output
https://ipywidgets.readthedocs.io/en/latest/examples/Output%20Widget.html
```py
self.err_viewer = widgets.Output()
with self.err_viewer:
    self.err_viewer.clear_output()
    print(error_message)
```
