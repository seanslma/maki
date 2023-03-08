# Blob

## blob with Python
```python
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
