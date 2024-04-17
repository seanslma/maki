# Blob
https://github.com/Azure-Samples/AzureStorageSnippets/blob/master/blobs/howto/python/blob-devguide-py/blob-devguide-blobs.py

https://learn.microsoft.com/en-us/samples/azure/azure-sdk-for-python/storage-blob-samples/

## when to use
- Ideal for storing **unstructured** data, like media files (videos, images, audio), logs, scientific data, and archives.
- Data is stored as objects called blobs, which can be very large (up to petabytes).
- Access is typically **programmatic** through code or APIs.
- Offers various access tiers for cost optimization based on access frequency.

## list blobs
https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-list-python
```PowerShell
ContainerClient.list_blobs      #name and metadata, tags, and other information associated with each blob
ContainerClient.list_blob_names #only blob name
ContainerClient.walk_blobs      #hierarchical listing
```

list blob storage containers with container resource_manager_id
```sh
az storage container list --account-name <storage-account-name> \
    --auth-mode login -o json
az storage container list --account-name <storage-account-name> \
    --auth-mode login --query "[].{Name:name, ResourceId:id}"
az storage container list --account-name <storage-account-name> \
    --account-key <storage-account-key> --query "[].{Name:name, ResourceId:id}"
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

m = 0
n = 0
for blob in container_client.walk_blobs(name_starts_with='2021/', delimiter='/'):
    if isinstance(blob, BlobPrefix):
        m += 1
        if m < 4:
            print(f'hierarchical: {blob.name}')
        #list_blobs_hierarchical(container_client, prefix=blob.name)
    else:
        n += 1
        if n < 4:
            print(f'normal blob: {blob.name}')
```

## blob size in a folder
```py
total_size = 0
for blob in container_client.walk_blobs(name_starts_with='2021/', delimiter='/'):
    total_size += blob.size
print(f'Total size: {total_size / 1024 / 1024} MB')
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
        source_blob.delete_blob()

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
