# Middleware

https://fastapi.tiangolo.com/tutorial/middleware/

A middleware is a function that works with every `request` before it is processed by any specific path operation. And also with every `response` before returning it.

## GZipMiddleware
https://docs.djangoproject.com/en/4.1/ref/middleware/

Handles GZip responses for any request that includes "gzip" in the Accept-Encoding header.

This middleware should be placed before any other middleware that need to read or write the response body so that compression happens afterward.

Must add header to work correctly:
```
app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000) #only compress when content body >= 1000 bytes

@router.get("/test")
def test_handler():
    content = {"test1": 1}
    headers = {"Accept-Encoding": "gzip"}
    return JSONResponse(content=content, headers=headers)
```
