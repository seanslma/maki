# Error handling

https://fastapi.tiangolo.com/tutorial/handling-errors/

## HTTPException
Use `HTTPException` to return HTTP responses with errors to the client.

The `detail` parameter can be a dict, a list, etc. They are handled automatically by FastAPI and converted to JSON.

```py
from fastapi import FastAPI, HTTPException

app = FastAPI()
items = {'foo': 'The Foo Wrestlers'}

@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return {'item': items[item_id]}
```

The detail can be get using `resp.json()`. Note that if there are no errors, `resp.json()` will return `[]`. 
If there are sever side errors, `resp.json()` will crash.
