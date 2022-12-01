# IO

## Convert async generator stream to file like object
https://stackoverflow.com/questions/59413796/how-to-convert-async-generator-stream-into-a-file-like-object-in-python3

May be can use `io.BytesIO` as well instead of `SpooledTemporaryFile`.
```
data_file = SpooledTemporaryFile(
    mode='w+b',
    max_size=MAX_RECEIVED_DATA_MEMORY_SIZE,
)
async for chunk in request.stream():
    data_file.write(chunk)
data_file.seek(0)
```
