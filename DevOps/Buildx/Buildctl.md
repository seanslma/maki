# Buildctl
https://github.com/moby/buildkit/blob/master/docs/reference/buildctl.md
```sh
buildctl [global options] command [command options] [arguments...]
```

## transition from docker to buildkit
https://dille.name/slides/2020-05-28/110_ecosystem/buildkit/transition.final/

## buildkitd address
Global option. Default: `unix:///run/buildkit/buildkitd.sock`
```sh
--addr tcp://buildkitd:1234
```

## deploy buildkit in kubernetes
https://kubernetes.courselabs.co/labs/buildkit/

## build
To build and push an image using Dockerfile:
```sh
buildctl build \
  --frontend dockerfile.v0 \
  --local context=. \
  --local dockerfile=./docker/linux/my-app.docker \
  --opt target=foo \
  --opt build-arg:foo=bar \
  --output type=image,name=docker.io/username/image,push=true
```

## cache: azure blob storage
```sh
--import-cache type=azblob,account_url=https://myaccount.blob.core.windows.net,name=my_image \  
--export-cache type=azblob,account_url=https://myaccount.blob.core.windows.net,name=my_image \
```

## metadata to file
```sh
--metadata-file metadata.json
```
