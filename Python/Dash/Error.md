# Error

## cannot import name 'dcc' from partially initialized module
```
cannot import name 'dcc' from partially initialized module 'dash' 
(most likely due to a circular import) (c:/.../dash.py)
```
One of the file is dash.py - should not name file `dash.py` as that would shadow the official dash module.

## A nonexistent object was used in an Input of a Dash callback
https://community.plotly.com/t/a-nonexistent-object-was-used-in-an-input-of-a-dash-callback-an-multipage-app/52007

in a multipage dashboard:
https://stackoverflow.com/questions/71361010/a-nonexistent-object-was-used-in-an-input-of-a-dash-callback-an-multipage-app

Solution???
```py
app.config['suppress_callback_exceptions'] = True
```

## error handling
https://flask.palletsprojects.com/en/2.2.x/errorhandling/

https://code-maven.com/python-flask-catch-exception

