# Blob

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
