# Web Server
https://github.com/tiangolo/fastapi/issues/2062

if using docker with kuberntes or some load balancer, i'll recommend:
`CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]`

After trying 
- `hypercorn` and `gunicorn` with 1 or 4 workers, 
- `hypercorn` with trio or default, 
- `gunicorn` with `uvicorn` worker 
I came to the conclusion that with the above configuration I got the **best results** when receiving many requests on endpoints that make several requests.

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

https://levelup.gitconnected.com/deploy-fastapi-with-hypercorn-http-2-asgi-8cfc304e9e7a
```py
hypercorn 'my_fastapi.fileapi:app' --bind 0.0.0.0:8080 --debug --reload --workers 2 --worker-class 'uvloop'
```

## gunicorn
`gunicorn` is a synchronous web server.
