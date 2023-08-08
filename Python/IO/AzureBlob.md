# Azure Blob Storage
https://learn.microsoft.com/en-us/azure/storage/files/storage-python-how-to-use-file-storage?tabs=python

## fsspec
### performance using `AzureBlobFileSystem`
When reading Parquet files from Azure Blob Storage using pd.read_parquet with the engine set to pyarrow, the performance can **become suboptimal**
when reading in parallel due to the limitations of the AzureBlobFileSystem and the way PyArrow handles parallel reading.

The main reason for this performance issue is that the `AzureBlobFileSystem`, which is used to interact with Azure Blob Storage, **does not natively support parallel reads efficiently**.
This limitation can lead to slower performance when multiple threads or processes are trying to read Parquet files in parallel from the same container in Azure Blob Storage.

```py
from fsspec import AbstractFileSystem
from azure.identity.aio import DefaultAzureCredential
def get_filesystem(
  account_name: str, 
  credential: object=None,
) -> AbstractFileSystem:
    from adlfs.spec import AzureBlobFileSystem
    from azure.identity.aio import DefaultAzureCredential
    # Disable messages from azure.identity.aio
    logging.getLogger('azure.identity.aio').setLevel(logging.ERROR)    
    credential = credential or DefaultAzureCredential()
    return AzureBlobFileSystem(
        account_name=account_name,
        credential=credential,
    )
```

## fsspec glob wildcards
https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html

performance
- use subfolders such as year/month will **siginificantly improve search performance**
- use wildcard characters in the middle will lead to full scan
- search a few sub folders one by one will be much faster
- 
```py
fs = get_filesystem(account_name='azure_blob_storage')
files = fs.glob('az://dev/2021/01/data*].parquet')
files = fs.glob('az://dev/2021/01/data[0-9][0-9].parquet')
```

## azure-blob-storage
`azure-blob-storage` supports both sync and async versions. 

When got this error
```
AttributeError: 'coroutine' object has no attribute 'token'
sys:1: RuntimeWarning: coroutine 'DefaultAzureCredential.get_token' was never awaited
```
It's most likely incorrectly used the async version `from azure.identity.aio import DefaultAzureCredential`.

## read parquet blob to df performance
`adlfs` can be 1.5-2x faster than `azure-blob-storage`. But `AzureBlobFileSystem` in parallel can be really slow down.
```py
from adlfs.spec import AzureBlobFileSystem
from azure.storage.blob import ContainerClient
from azure.identity import DefaultAzureCredential

def read_parquet_fast(path: str, columns: list[str]) -> pd.DataFrame:
    fs = AzureBlobFileSystem(
        account_name=account_name,
        credential=DefaultAzureCredential(),
    )
    with fs.open(path) as f:
        df = pd.read_parquet(path=f, columns=columns)
    return df

def read_parquet_slow(path: str, columns: list[str]) -> pd.DataFrame:
    path = path.split('/', 3)[-1]
    container_client = = ContainerClient(
        account_url=f'https://{account_name}.blob.core.windows.net',
        credential=DefaultAzureCredential(),
        container_name=container_name,
    )
    with io.BytesIO() as data_buffer:
        blob_client = container_client.get_blob_client(path)
        blob_client.download_blob().readinto(data_buffer)
        data_buffer.seek(0)
        df = pd.read_parquet(data_buffer, columns=columns, engine='pyarrow')
    return df
```

## Azure Data Lake Storage (ADLS)
It's actually created on top of `azure-storage-blob`.
The `azure-storage-file-datalake` library is specifically designed to interact with Azure Data Lake Storage Gen2 (ADLS Gen2). 
ADLS Gen2 is an enterprise-grade distributed file system built on top of Azure Blob Storage, providing hierarchical namespace and capabilities for big data analytics.

When working with Azure Data Lake Storage Gen2, we should use "azure-storage-filedatalake" and for general-purpose object storage in Azure Blob Storage, should use "azure-blob-storage"
