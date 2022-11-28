# Middleware

https://fastapi.tiangolo.com/tutorial/middleware/

A middleware is a function that works with every `request` before it is processed by any specific path operation. And also with every `response` before returning it.

## GZipMiddleware
Handles GZip responses for any request that includes "gzip" in the Accept-Encoding header.
