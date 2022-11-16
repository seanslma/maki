# FastAPI
https://dev.to/jbrocher/fastapi-testing-a-database-5ao5

## model
https://fastapi.tiangolo.com/tutorial/body/

https://realpython.com/fastapi-python-web-apis/

- `request body` is the data sent by client to server. 
- `response body` is the data the API sends back to the client.

If a parameter is not present in the path and it also uses **Pydantic BaseModel**, FastAPI automatically considers it as a request body. 

FastAPI will read the incoming request payload as JSON and convert the corresponding data types if needed. Also, it will perform validation and return an appropriate error response.

## postgresql
https://www.educative.io/answers/how-to-use-postgresql-database-in-fastapi

## test
https://fastapi.tiangolo.com/tutorial/testing/
