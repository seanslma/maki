# FastAPI
https://fastapi.tiangolo.com/tutorial

## test 
```
if __name__ == '__main__':
    uvicorn.run('api.main:app', host='127.0.0.1', port=8000)
```
or run in terminal
`uvicorn 'api.main:app' --host '127.0.0.1' --port 8000`

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
