# Response

## custom response
https://fastapi.tiangolo.com/advanced/custom-response/

## FileResponse
will save the file on disk and return a path.

## Json response
The default one useing `jsonable_encoder` is at least **5x** slower than `df.to_json`.
```
df.fillna('').to_dict(orient='records') #default
JSONResponse(jsonable_encoder(df.fillna('').to_dict(orient='records'))) #default equvalent
Response(df.fillna('').to_json(orient='records', date_format='iso', date_unit='s'), media_type="application/json") #df.to_json
resp.headers['Accept-Encoding'] = "gzip"  #seems not required! use gzip, can have similar performance compared to parquet file
```

## StreamingResponse
requires an iterator object to send the results in chunks.

https://cloudbytes.dev/snippets/received-return-a-file-from-in-memory-buffer-using-fastapi

Return a parquet file (similar performance to json)
```
bio = io.BytesIO()
df.to_parquet(bio)
bio.seek(0)
resp = StreamingResponse(bio, media_type="bytes/parquet")
resp.headers["Content-Disposition"] = f"attachment; filename=data.parquet"
```

## return an image
https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi
```
byte_im = BytesIO()
image.save(byte_im, "JPEG")
byte_im.seek(0)   #get byte_im size: byte_im.getbuffer().nbytes

return StreamingResponse(byte_im, media_type="image/jpeg")
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

parquet is 4x faster than json and 8x faster than csv. Why csv is slow?
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
        resp = StreamingResponse(io.StringIO(df.to_csv(index=False)), media_type='text/csv')
        resp.headers['Content-Disposition'] = 'attachment; filename=data.csv'
        resp.headers['Accept-Encoding'] = 'gzip' #much slower than json - a bug?
    elif request.headers.get('Accept') == 'bytes/parquet':
        byio = io.BytesIO()
        df.to_parquet(byio)
        byio.seek(0)
        resp = StreamingResponse(byio, media_type='bytes/parquet')
        resp.headers['Content-Disposition'] = 'attachment; filename=data.parquet'
        resp.headers['Accept-Encoding'] = 'gzip'
    else:
        content = df.fillna('').to_json(orient='records', date_format='iso', date_unit='s')
        resp = Response(content, media_type='application/json')       
        resp.headers['Accept-Encoding'] = 'gzip'
    return resp
    
def api_headers(header_type):
    if header_type == 'json':
        return None
    elif header_type == 'csv':
        return {"Accept":"text/csv"}
    elif header_type == 'parquet':
        return {"Accept":"bytes/parquet"}
    else:
        return None
        
def req_to_df(req, header_type):
    if header_type == 'json':
        return pd.read_json(req.content.decode('utf-8'))
    elif header_type == 'csv':
        return pd.read_csv(io.StringIO(req.content.decode('utf-8')))
    elif header_type == 'parquet':
        return pd.read_parquet(io.BytesIO(req.content))
    else:
        return None
        
def api_get(url, header_type='json'):
    headers = api_headers(header_type)
    req = requests.get(url, headers=headers)
    df = req_to_df(req, header_type)
    return df
```
