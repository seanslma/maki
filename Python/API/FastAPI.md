# FastAPI
https://fastapi.tiangolo.com/tutorial

FastAPI is an ASGI framework
- the resulting app object doesn't talk HTTP directly, 
- it just receives dictionaries and stuff passed by the ASGI server, 
- and that's how it handles the rest.

You need something to pass those arguments to the FastAPI app. It could be Uvicorn, Hypercorn, Daphne... etc.

https://github.com/tiangolo/fastapi/issues/2062
- FastAPI is based on Starlette, Starlette is an ASGI micro-framework/toolkit. 
- Uvicorn is made/maintained by the same developer(s) as Starlette. 
- They are not tightly coupled or depend on each other in any way, but are the natural closest match.

By default, if you install with pip install `uvicorn[standard]` that will include and use Uvloop, a drop-in replacement for the asyncio loop, with **very high performance**. You don't have to do anything in your code to use it, just install `uvicorn[standard]`.

That `Uvloop` thing is what gives all the performance to anything (or almost anything) in async Python that has high performance. So, chances are Uvloop would give the best performance.

## test 
```
if __name__ == '__main__':
    uvicorn.run('api.main:app', host='127.0.0.1', port=8000)
```
or run in terminal
`uvicorn 'api.main:app' --host '127.0.0.1' --port 8000 --reload`

## bigger application structure
https://fastapi.tiangolo.com/tutorial/bigger-applications/

## model
https://fastapi.tiangolo.com/tutorial/body/

https://realpython.com/fastapi-python-web-apis/

- `request body` is the data sent by client to server. 
- `response body` is the data the API sends back to the client.

If a parameter is not present in the path and it also uses **Pydantic BaseModel**, FastAPI automatically considers it as a request body. 

FastAPI will read the incoming request payload as JSON and convert the corresponding data types if needed. Also, it will perform validation and return an appropriate error response.

## postgresql
https://dev.to/jbrocher/fastapi-testing-a-database-5ao5

https://www.educative.io/answers/how-to-use-postgresql-database-in-fastapi

https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396

## test
https://fastapi.tiangolo.com/tutorial/testing/
