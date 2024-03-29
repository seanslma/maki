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

cli
```sh
uvicorn 'my_fastapi.fileapi:app' --host '127.0.0.1' --port 7000 --loop 'uvloop' --workers 1 --root-path '/api' --reload
```

```py
import uvicorn
uvicorn.run(
    'my.api.main:app',
    host='127.0.0.1',
    port=7000,
    reload=False,
)
```

Settings:
https://www.uvicorn.org/settings/
- `--loop`: The `uvloop` implementation provides greater performance, but is **not compatible** with Windows or PyPy.
- Underwindows windows can use loop `asyncio`.

## hypercorn
`Hypercorn` is an asynchronous ASGI web server.
It can use `uvloop` as Uvicorn does, or use other event loops. It supports HTTP/2.

Config:
https://pgjones.gitlab.io/hypercorn/how_to_guides/configuring.html

https://levelup.gitconnected.com/deploy-fastapi-with-hypercorn-http-2-asgi-8cfc304e9e7a
```sh
hypercorn 'my_fastapi.fileapi:app' --bind 127.0.0.1:5000 --worker-class 'uvloop' --workers 2 --root-path '/api' --reload --debug
```

```py
#import uvloop
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

import os
os.environ['HYPERCORN_WORKERS'] = '2'
os.environ['HYPERCORN_DEBUG'] = 'False'
os.environ['HYPERCORN_ROOT_PATH'] = 'c:/api'

config = Config()
config.bind = ['127.0.01:8000']
#config.worker_class = uvloop.Loop # uvloop only for linux
#config.use_reload = auto_reload
config.accesslog = '-'
asyncio.run(serve(app, config))
```

more example
```py
import click
#import uvloop
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from . import __version__
from .routers import (
    dev,
    tst,
)

app = FastAPI(
    title='Dev REST API',
    version=__version__,
    docs_url='/',
)

app.add_middleware(GZipMiddleware, minimum_size=100000)

app.include_router(sales.router, prefix='/sales', tags=['Sales'])
app.include_router(marketing.router, prefix='/marketing', tags=['Marketing'])

import os
os.environ['HYPERCORN_WORKERS'] = '2'
os.environ['HYPERCORN_DEBUG'] = 'False'
os.environ['HYPERCORN_ROOT_PATH'] = 'c:/test/api'

@click.command()
@click.option('--host', type=click.STRING, default='127.0.0.1')
@click.option('--port', type=click.INT, default=7000)
@click.option('--auto-reload/--no-auto-reload', default=True)
def cli(**kwargs):
    host = kwargs['host']
    port = kwargs['port']
    auto_reload = kwargs['auto_reload']
    config = Config()
    config.bind = [f'{host}:{port}']
    #config.worker_class = uvloop.Loop # uvloop only for linux
    #config.use_reload = auto_reload
    #config.accesslog = '-'
    asyncio.run(serve(app, config))
```

## gunicorn
`gunicorn` is a synchronous web server.
