# IO

## adlfs
**cavaet**: The `AzureBlobFileSystem` in `adlfs` does not support concurrent read/write. 
```py
from adlfs.spec import AzureBlobFileSystem
from azure.identity.aio import DefaultAzureCredential

fs = AzureBlobFileSystem(
    account_name=account_name,
    credential=DefaultAzureCredential(),
)

with fs.open(path) as f:
    df = pd.read_parquet(path=f, columns=columns)
```

If use `ManagedIdentityCredential` will get this error: ManagedIdentityCredential authentication unavailable, no response from the IMDS endpoint.

## Azure Storage Blob: Read parquet file to df
```py
# option 1
blob_name = 'dev/data.parquet'
blob_client = container.get_blob_client(blob=blob_name)
stream_downloader = blob_client.download_blob()

stream = BytesIO()
stream_downloader.readinto(stream)
df = pd.read_parquet(stream, engine='pyarrow')

# option 2
stream_downloader = container_client.download_blob(blob_name)
stream = BytesIO(stream_downloader.readall())
df = pd.read_parquet(stream, engine='pyarrow')
```
## Azure Storage Blob: Write df to parquet file
Method 1: using pandas and adlfs (seems not working 100% when file too large), also adlfs not support concurrent read/write
```py
from adlfs import AzureBlobFileSystem
# create file system
fs = AzureBlobFileSystem(
    account_name = '<AZURE_STORAGE_ACCOUNT>',
    credential = DefaultAzureCredential(),
)
# read parquet from azure blob storage
with fs.open(filepath) as f:
    df = pd.read_parquet(f)
df = pq.read_table(filepath, filesystem=fs).to_pandas() #another way
# write parquet to azure blob storage
with fs.open(filepath, mode='wb') as f:
    df.to_parquet(f)
```

Method 2: convert df to bytes first
https://stackoverflow.com/questions/54664712/how-to-store-pandas-dataframe-data-to-azure-blobs-using-python

- use `io.BytesIO`
- Apache Arrow `BufferOutputStream`: writes to the stream without the overhead of going through Python, less copies are made and the GIL is released
```py
import io
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# get blob client
credential = DefaultAzureCredential()
blob_service = BlobServiceClient(
    account_url="https://<my_account_name>.blob.core.windows.net",
    credential=credential,
)
blob_client = blob_service.get_blob_client(
    container=container_name,
    blob=blob_path,
)

# upload file: method 1
parquet_bytes = io.BytesIO()
df.to_parquet(parquet_bytes, engine='pyarrow')
parquet_bytes.seek(0)  # change the stream position back to the beginning after writing
blob_client.upload_blob(data=parquet_bytes)

# upload file: method 2
table = pa.Table.from_pandas(df)
buf = pa.BufferOutputStream()
pq.write_table(table=table, where=buf, compression='zstd')
blob = buf.getvalue()
buf = pa.py_buffer(blob) #buf.to_pybytes() will make a copy of the data
with fs.open(filepath, mode='wb') as f:
    f.write(buf)
```

