# IO

## Convert sync to async
```py
async def to_async(iterator):
    for i in iterator:
        yield i
```

## Convert async generator stream to file like object
https://stackoverflow.com/questions/59413796/how-to-convert-async-generator-stream-into-a-file-like-object-in-python3

Maybe can use `io.BytesIO` as well instead of `SpooledTemporaryFile`.
```py
data_file = SpooledTemporaryFile(
    mode='w+b',
    max_size=MAX_RECEIVED_DATA_MEMORY_SIZE,
)
async for chunk in request.stream():
    data_file.write(chunk)
data_file.seek(0)
```
