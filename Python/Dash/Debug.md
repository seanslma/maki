# Debug

https://towardsdatascience.com/advancing-to-professional-dashboard-with-python-using-dash-and-plotly-1e8e5aa4c668

```
app.run(debug=True, host=host, port=port)
```

## debugging decorator
```py
debug_mode = True #enable debug

def print_callback(debug_mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if debug_mode:
                print(f'===> Func: {func.__name__}')
                input_triggers = ', '.join([t['prop_id'] for t in dash.callback_context.triggered}])
                print(f'Triggered by: {input_triggers')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.callback(...)
@print_callback(debug_mode)
def my_func(trigger):
    pass
```
