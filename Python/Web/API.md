# API

## fastAPI
https://fastapi.tiangolo.com/tutorial/body/

https://realpython.com/fastapi-python-web-apis/

- `request body` is the data sent by client to server. 
- `response body` is the data the API sends back to the client.

If a parameter is not present in the path and it also uses **Pydantic BaseModel**, FastAPI automatically considers it as a request body. 

FastAPI will read the incoming request payload as JSON and convert the corresponding data types if needed. Also, it will perform validation and return an appropriate error response.

### HTTP error 422: Unprocessable Entity
https://progressivecoder.com/a-guide-to-fastapi-request-body-using-pydantic-basemodel/

## REST API
Most standard (json) for web-based APIs.

## GraphQL
Client can specify just the information they need, which can greatly reduce duplicate or unnecessary data being transmitted.
 
## gRPC
for fast transport, leveraging HTTP/2.
