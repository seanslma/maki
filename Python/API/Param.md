# Parameter

## Header parameter
https://fastapi.tiangolo.com/tutorial/header-params/

Get the header as an input parameter
```sh
from typing import Optional
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}
```
