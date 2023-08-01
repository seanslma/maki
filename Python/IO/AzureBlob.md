# Azure Blob Storage
https://learn.microsoft.com/en-us/azure/storage/files/storage-python-how-to-use-file-storage?tabs=python

## fsspec
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
- use subfolders such as year/month will siginificantly improve search performance
- use wildcard characters in the middle will lead to full scan
- search a few sub folders one by one will be much faster
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
