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

## Azure Storage Blob
