# FlaskCaching

## Example
```py
from flask_caching import Cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'SimpleCache' #'filesystem',
    #'CACHE_DIR': 'cache-directory'
})

@cache.memoize(timeout=CACHE_TIMEOUT)
def my_func():
    return df
```
