# Web Server
https://github.com/tiangolo/fastapi/issues/2062

## uvicorn
`uvicorn` is an asynchronous ASGI web server. 
It uses `uvloop` if it can. 
Uvicorn supports HTTP/1.1 and WebSockets, but does not (yet) support HTTP/2.

```py
uvicorn 'my_fastapi.fileapi:app' --host '127.0.0.1' --port 8000 --reload
```

## hypercorn
`Hypercorn` is an asynchronous ASGI web server. 
It can use `uvloop` as Uvicorn does, or use other event loops. It supports HTTP/2. 

## gunicorn
`gunicorn` is a synchronous web server.
