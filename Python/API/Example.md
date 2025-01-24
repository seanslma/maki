# Example

## test api function
```py
from fastapi import FastAPI, APIRouter, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from datetime import date, datetime
from typing import Union, Optional
from json import dumps
import pydantic_core

app = FastAPI()
router = APIRouter()
client = TestClient(app)

class SHA256(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Union[bytes, str], values: Optional[dict] = None) -> str:
        if isinstance(v, bytes):
            v = v.hex()

        if not isinstance(v, str):
            raise TypeError('Must be string or bytes')

        if len(v) != 64:
            raise TypeError('String must be 64 characters')

        return v

class MyModel_i(BaseModel):
    sha256_hash: str 

class MyModel_o(BaseModel):
    sha256_hash: SHA256
    class Config:
        from_attributes = True
        
@router.post("/myapp", response_model=dict, status_code=status.HTTP_201_CREATED)
def myapp_test(
    params: MyModel_o,
) -> dict:
    return params.model_dump()
app.include_router(router)

data = dumps(MyModel_i(
    sha256_hash=hashlib.sha256('xyz'.encode('utf-8')).hexdigest()
).model_dump())
response = client.post("/myapp", data=data)

# Assert status code is 201 (created)
print(response.status_code)

# Check that the returned task is correct
response_data = response.json()
print(response_data)
```
