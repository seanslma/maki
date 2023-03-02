# Response Types

## custom response
https://fastapi.tiangolo.com/advanced/custom-response/

## FileResponse
will save the file on disk and return a path.

## JSONResponse
`**caveat**`: For file larger than 250MB, when using `pd.read_json` will get error: `Could not reserve memory block`

### Option 1: default
The default one useing `jsonable_encoder` (return list of jsons) is at least **5x** slower than `df.to_json`.
```
resp = df.fillna('').to_dict(orient='records') #default
df = pd.DataFrame.from_dict(req.json())        #a - 5-20% faster than b
df = pd.read_json(io.BytesIO(req.content))     #b - 5-15% faster than c
df = pd.read_json(req.content.decode('utf-8')) #c - slowest

resp = JSONResponse(jsonable_encoder(df.fillna('').to_dict(orient='records'))) #default equvalent
```

### Option 2: df.to_json
5 - 10x faster than default
```
content = df.fillna('').to_json(orient='records', date_format='iso', date_unit='s') #df.to_json
resp = Response(content, media_type="application/json")

resp.headers['Accept-Encoding'] = 'gzip'  #seems not required for gzip compression!
```

## Response
Use `Response` if cache is required (much faster than StreamingResponse)
- Response only supports `string` or `bytes`
- `io.BytesIO.getvalue()` changes file like object to bytes
```
bio = io.BytesIO(df.to_parquet(compression='brotli')).getvalue()
bio = io.BytesIO(df.to_parquet(compression=None)).getvalue() #compared to compression, faster but slower for cached data
resp = Response(bio, media_type="bytes/parquet") #Response only support string or bytes
resp.headers["Content-Disposition"] = 'attachment; filename=data.parquet'

df = pd.read_parquet(io.BytesIO(req.content)) #cannot use `pd.read_parquet(url)` expect url like a file object not bytes
```

## StreamingResponse
When send a large amount of data, e.g., 50 MB, through API, we might get timeout, other network issues for downloading such a data from the server. Streaming response will ensure the data being downloaded chunk by chunk to avoid these issues.

**requires an iterator object to send the results in chunks.**

https://cloudbytes.dev/snippets/received-return-a-file-from-in-memory-buffer-using-fastapi

### return a parquet file (similar performance to json)
**Note**: StreamingResponse is very slow compared to Response.

Due to the content BytesIO not `typing.AsyncIterable`? https://github.com/tiangolo/fastapi/issues/2302
```
#bio = io.BytesIO()
#df.to_parquet(bio)
#bio.seek(0) #can use .getvalue() .getbuffer().nbytes
bio = io.BytesIO(df.to_parquet(compression='brotli'))
resp = StreamingResponse(bio, media_type="bytes/parquet")
resp.headers["Content-Disposition"] = 'attachment; filename=data.parquet'
df = pd.read_parquet(io.BytesIO(req.content))
```

Solution: Convert the content to async now ony a little slower than using Response.
```py
def generate():
    with bio as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            yield chunk
resp = StreamingResponse(generate(), media_type="bytes/parquet")
```

### return an image
https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi
```
byte_im = BytesIO()
image.save(byte_im, 'JPEG')
byte_im.seek(0)   #get byte_im size: byte_im.getbuffer().nbytes

return StreamingResponse(byte_im, media_type='image/jpeg')
```

Another solution: faster?

https://stackoverflow.com/questions/66223811/how-to-increase-transfer-speed-when-posting-an-image-to-a-rest-api
```
data = {'shape': image.shape, 'img': base64.b64encode(image.tobytes())}
image = np.frombuffer(base64.b64decode(data.img)).reshape(data.shape)
```

## api get
https://stackoverflow.com/questions/73564771/fastapi-is-very-slow-in-returning-a-large-amount-of-json-data

To prevent browser show large amount of data
- set `Content-Disposition` header to Response using the `attachment` parameter and passing a filename

**Performance**
- parquet (Response) is 2x faster than json (Response)
- json (Response) is 2x (5MB, 1x 50MB) faster than parquet (StreamingResponse), will return bytes
- json is 8x faster than csv. Why csv is slow - not well compressed compared to json and require more time to parse?
```
import io
import requests
import pandas as pd

@router.get("/get_df",
    status_code=status.HTTP_200_OK,
    description='Test api get',
)
async def get_df(
    request: Request,
):
    df = pd.DataFrame([['i',1],['j', 2]], columns=['k', 'v'])

    if request.headers.get('Accept') == 'text/csv':
        content = io.StringIO(df.to_csv(index=False))
        resp = StreamingResponse(content, media_type='text/csv')
        resp.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    elif request.headers.get('Accept') == 'bytes/parquet':
        content = io.BytesIO(df.to_parquet(compression='brotli'))
        resp = StreamingResponse(content, media_type='bytes/parquet')
        resp.headers['Content-Disposition'] = 'attachment; filename=data.parquet'
    else:
        content = df.fillna('').to_json(orient='records', date_format='iso', date_unit='s')
        resp = Response(content, media_type='application/json')
    return resp

def url_to_df(url, header_type):
    #only for StreamingResponse type except json
    if header_type == 'csv':
        return pd.read_csv(url, storage_options={'Accept':'text/csv'})
    elif header_type == 'parquet':
        return pd.read_parquet(url, storage_options={'Accept':'bytes/parquets'})
    else: #json
        return pd.read_json(url, storage_options={'Accept':'application/json'})

def req_to_df(url, header_type):
    if header_type == 'csv':
        req = requests.get(url, headers={"Accept":"text/csv"})
        return pd.read_csv(io.StringIO(req.content.decode('utf-8')))
    elif header_type == 'parquet':
        req = requests.get(url, headers={"Accept":"bytes/parquet"})
        return pd.read_parquet(io.BytesIO(req.content))
    else: #json
        req = requests.get(url, headers={'Accept':'application/json'})
        return pd.DataFrame.from_dict(req.json()))

def api_get(url, header_type='json', faster=True):
    if faster: #30% faster
        df = url_to_df(url, header_type)
    else:
        df = req_to_df(url, header_type)
    return df
```
