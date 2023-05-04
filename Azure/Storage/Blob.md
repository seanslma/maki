# Blob
https://github.com/Azure-Samples/AzureStorageSnippets/blob/master/blobs/howto/python/blob-devguide-py/blob-devguide-blobs.py

## list blobs
https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-list-python
```py
ContainerClient.list_blobs      #name and metadata, tags, and other information associated with each blob
ContainerClient.list_blob_names #only blob name
ContainerClient.walk_blobs      #hierarchical listing
```

example
```py
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, BlobLeaseClient, BlobPrefix, ContentSettings

account_name = '<account_name>'
container_name = '<container_name>'

account_url = f"https://{account_name}.blob.core.windows.net"
credential = DefaultAzureCredential()

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=credential)
container_client = blob_service_client.get_container_client(container=container_name)

m =0
n =0
for blob in container_client.walk_blobs(name_starts_with='2021/', delimiter='/'):
    if isinstance(blob, BlobPrefix):
        m +=1
        if m < 4:
            print(f'hierarchical: {blob.name}')
        #list_blobs_hierarchical(container_client, prefix=blob.name)
    else:
        n +=1
        if n < 4:
            print(f'normal blob: {blob.name}')
```

## move blob
limitations: creation_time and last_modified cannot be preserved and cannot be updated

can we do this? No! 'BlobClient' object has no attribute 'set_blob_properties'
```py
# Set the creation time of the destination blob to match the creation time of the source blob
dest_blob_properties = dest_blob_client.get_blob_properties()
dest_blob_properties.creation_time = blob_properties.creation_time
dest_blob_client.set_blob_properties(blob_properties=dest_blob_properties)
```

```py
def move_blob(
    container_client: ContainerClient,
    source_blob_fullpath: str,
    dest_blob_path: str,
):
    """
    Move blob file to another folder in the same blob container
    """
    # Make sure source blob exists
    source_blob = container_client.get_blob_client(blob=source_blob_fullpath)
    if source_blob.exists():
        # Lease source blob during copy to prevent other clients from modifying it
        lease = BlobLeaseClient(client=source_blob)
        lease.acquire(-1) # Create an infinite lease

        # Get source blob properties
        source_blob_properties = source_blob.get_blob_properties()

        # Copy blob
        blob_filename = source_blob_fullpath.rsplit('/', 1)[-1]
        dest_blob = container_client.get_blob_client(blob=f'{dest_blob_path}/{blob_filename}')
        dest_blob.start_copy_from_url(source_url=source_blob.url)

        # Break source blob lease
        if source_blob_properties.lease.state == "leased":
            lease.break_lease()

        # Delete source blob
        #source_blob.delete_blob()

        return source_blob_properties
```

## blob with Python
```py
import os, uuid
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, __version__

#create BlobServiceClient
blobsvc = BlobServiceClient.from_connection_string('blob connection string')

#create container with a unique name
container_name = str(uuid.uuid4())
container = blobsvc.create_container(container_name)

#create blob client
client = client_blobsvc.get_blob_client(container=container_name, blob=filename)

#upload file to blob
with open(f'{filename}.txt', "rb") as data:
    client.upload_blob(data)

#list blobs in container
blob_list = container.list_blobs()
for blob in blob_list:
    print("\t" + blob.name)

#download blob to a local file
with open(download_file, "wb") as file:
    file.write(client.download_blob().readall())

#deleting blob container
container.delete_container()
```

## upload file
```py
import uuid
def file_to_blob(local_filepath, blob_filepath, chunk_size = 4 * 1024 * 1024):
    """
    Upload file to blob storage
    """
    try:
        blob_client = self.container_client.get_blob_client(blob_filepath)
        block_list = []
        with open(local_filepath,'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                blk_id = str(uuid.uuid4())
                blob_client.stage_block(block_id=blk_id, data=chunk)
                block_list.append(BlobBlock(block_id=blk_id))
        blob_client.commit_block_list(block_list)
    except Exception as exc:
        print('Upload file error')
```

## write df to parquet file
Method 1: using pandas (seems not working 100% when file too large)
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
