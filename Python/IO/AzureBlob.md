# Azure Blob Storage
https://learn.microsoft.com/en-us/azure/storage/files/storage-python-how-to-use-file-storage?tabs=python

## fsspec
If the path ends with `/`, **only folders** are returned.

## adlfs
**Not correct**: performance using `AzureBlobFileSystem`
```
When reading Parquet files from Azure Blob Storage using pd.read_parquet with the engine set to pyarrow,
the performance can **become suboptimal** when reading in parallel due to the limitations of the
AzureBlobFileSystem and the way PyArrow handles parallel reading.

The main reason for this performance issue is that the `AzureBlobFileSystem`, which is used to interact with
Azure Blob Storage, **does not natively support parallel reads efficiently**. This limitation can lead to
slower performance when multiple threads or processes are trying to read Parquet files in parallel from
the same container in Azure Blob Storage.
```

### create file system
```py
from adlfs.spec import AzureBlobFileSystem
from azure.identity.aio import DefaultAzureCredential
def get_file_system(
  account_name: str,
  credential: object=None,
) -> AzureBlobFileSystem:
    # Disable messages from azure.identity.aio
    logging.getLogger('azure.identity.aio').setLevel(logging.ERROR)
    credential = credential or DefaultAzureCredential()
    return AzureBlobFileSystem(
        account_name=account_name,
        credential=credential,
    )
```

### `fs.glob` vs `fs.ls`
- `fs.glob('container-name/xyz-*.parquet')` is supper slow - will scan all files in this container
- `fs.ls(path='container-name', prefix='xyz-')` is much faster - will only list folders (not subfolders) and files in the path
- but `fs.ls` will crash if the folder not exist

### adlfs parallel performance
`pd.read_parquet` is 2-3x faster than `dd.read_parquet`. Do not create the file system for each parallel call - can be slow.
```py
def read_parquet_file(
    *,
    fs: AzureBlobFileSystem,
    path: str,
    columns: list[str],
    filters: list[tuple] = None,
) -> pd.DataFrame:
    """
    The `path` should be in this format `az://<blob-name>/folder/file-name`
    """
    # Occasionally it will fail to retrieve a token
    retries = 3     # Number of retries
    retry_delay = 2 # Seconds to wait between retries
    while retries > 0:
        try:
            with fs.open(path) as f:
                df = pd.read_parquet(
                    path=f, columns=columns, filters=filters, engine='pyarrow'
                )
            break
        except ClientAuthenticationError:
            retries -= 1
            if retries > 0:
                time.sleep(retry_delay)
            else:
                raise
        except Exception:
            raise
    return df

def read_parquet_files(
    paths: list[str],
    columns: list[str],
    filters: list[tuple] = None,
    use_cache: bool = False,
) -> list[pd.DataFrame]:
    """
    Read multiple parquet files in parallel into a list of pd.DataFrame
    """
    if not filters:
        filters = None
    # do not create the file system for each thread call, can be very slow
    fs = get_file_system()
    if len(paths) == 1:
        dfs = [
            read_parquet_file(fs=fs, path=paths[0], columns=columns, filters=filters)
        ]
    else:
        n_jobs = min(cpu_count(), len(paths))
        with ThreadPool(processes=n_jobs) as pool:
            dfs = pool.map(
                lambda path:
                    read_parquet_file(fs=fs, path=path, columns=columns, filters=filters),
                paths,
            )
    return dfs

# can be 2-3x faster than dd.read_parquet
dfs = read_parquet_files(
    paths=paths,
    columns=columns,
    filters=filters,
)
d1 = pd.concat(dfs, axis=0).reset_index().get(columns)

# can 2-3x slower than pd.read_parquet
d2 = dd.read_parquet(
    paths,
    index=False,
    columns=columns,
    filters=filters,
    engine='pyarrow',
    storage_options=storage_options,
    open_file_options=dict(precache_options={'method': 'parquet'}),
    schema=schema,
).compute()
```

### adlfs glob wildcards performance
https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html

performance
- use subfolders such as year/month will **siginificantly improve search performance**
- use wildcard characters in the middle will lead to full scan
- search a few sub folders one by one will be much faster

```py
files = fs.glob('dev-blob/2021/01/data*].parquet')
files = fs.glob('dev-blob/2021/01/data[0-9][0-9].parquet')
```

## azure-storage-blob
- can be 2-3x slower than `adlfs`
- `azure-storage-blob` supports both sync and async versions.

When got this error
```
AttributeError: 'coroutine' object has no attribute 'token'
sys:1: RuntimeWarning: coroutine 'DefaultAzureCredential.get_token' was never awaited
```
It's most likely incorrectly used the async version `from azure.identity.aio import DefaultAzureCredential`.

## read parquet blob to df performance
`adlfs` can be 1.5-2x faster than `azure-storage-blob`.
But `AzureBlobFileSystem` in parallel can be really slow down if used incorrectly
(**do not create a separate fs for each parallel run - can be very slow**).
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
