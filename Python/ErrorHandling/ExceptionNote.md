# Exception Note

## add extra info to exception
https://stackoverflow.com/questions/6062576/adding-information-to-an-exception
```py
try:
    raise TypeError('Bad type.')
except Exception as e:
    raise type(e)('Extra info.') from e
```

With PEP 678 (Python 3.11) adding notes to exceptions is natively supported
```py
try:
    raise TypeError('Bad type.')
except Exception as e:
    e.add_note('Extra info.')
    raise
```
