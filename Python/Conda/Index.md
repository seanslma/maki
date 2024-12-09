# Index
The conda index command is particularly useful when you're hosting your own conda package channel, 
either on a local server or on a cloud storage service like AWS S3 or Azure Blob Storage. 
It allows you to manage and update the channel's index files, ensuring that users can easily discover and install packages from your channel.

## separated from conda-build
https://conda.github.io/conda-index/

## create index for a channel
https://docs.conda.io/projects/conda-build/en/stable/concepts/generating-index.html
```sh
conda index channel_path # conda index channels/conda-forge
```
