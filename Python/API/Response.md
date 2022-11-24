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

## api get
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
        response = StreamingResponse(io.StringIO(df.to_csv(index=False)), media_type="text/csv")
        response.headers["Content-Disposition"] = f"attachment; filename=meter_data.csv"
        return response
    elif request.headers.get('Accept') == 'bytes/parquet':
        byio = io.BytesIO()
        df.to_parquet(byio)
        byio.seek(0)
        response = StreamingResponse(byio, media_type="bytes/parquet")
        response.headers["Content-Disposition"] = f"attachment; filename=file.parquet"
        return response
    else:
        return df.fillna('').to_dict(orient='records')

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
        return pd.DataFrame.from_dict(req.json())
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
