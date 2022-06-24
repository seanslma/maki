# Dashboard

## Output logging info from dashboard
Not good:

https://ipywidgets.readthedocs.io/en/latest/examples/Output%20Widget.html

Simple and effective:
```
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
