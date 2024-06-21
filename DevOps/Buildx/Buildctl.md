# Buildctl
https://github.com/moby/buildkit/blob/master/docs/reference/buildctl.md

## build
To build and push an image using Dockerfile:
```sh
buildctl build \
  --frontend dockerfile.v0 \
  --opt target=foo \
  --opt build-arg:foo=bar \
  --local context=. \
  --local dockerfile=. \
  --output type=image,name=docker.io/username/image,push=true
```

## azure blob storage cache
```sh
--import-cache type=azblob,account_url=https://myaccount.blob.core.windows.net,name=my_image \  
--export-cache type=azblob,account_url=https://myaccount.blob.core.windows.net,name=my_image \
```

## metadata to file
```sh
--metadata-file metadata.json
```
