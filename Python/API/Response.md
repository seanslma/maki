# Response

## custom response
https://fastapi.tiangolo.com/advanced/custom-response/

https://stackoverflow.com/questions/73564771/fastapi-is-very-slow-in-returning-a-large-amount-of-json-data

## FileResponse
will save the file on disk and return a path.

## StreamingResponse
requires an iterator object to send the results in chunks.

https://cloudbytes.dev/snippets/received-return-a-file-from-in-memory-buffer-using-fastapi

## return an image
https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi
```
byte_im = BytesIO()
image.save(byte_im, "JPEG")
byte_im.seek(0)

return StreamingResponse(byte_im, media_type="image/jpeg")
```
