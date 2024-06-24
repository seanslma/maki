# Buildctl
https://github.com/moby/buildkit/blob/master/docs/reference/buildctl.md
```sh
buildctl [global options] command [command options] [arguments...]
```

## transition from docker to buildkit
https://dille.name/slides/2020-05-28/110_ecosystem/buildkit/transition.final/

example
```sh
docker build \
    . -f ./docker/linux/my-app.docker \
    --build-arg name=my-app \
    --no-cache --force-rm \
    -t docker.example.com/uat/my-app:0.1.0

buildctl build \
    --frontend dockerfile.v0 \
    --local context=. \
    --local dockerfile=./docker/linux/ \ # can only be a directory
    --opt filename=my-app.docker \       # the dockerfile name
    --opt build-arg:name=my-app \  
    --opt no-cache=true   
    --output type=image,name=docker.example.com/uat/my-app:0.1.0
```

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
    --local dockerfile=./docker/linux/ \ # can only be a directory
    --opt filename=my-app.docker \       # the dockerfile name
    --opt target=foo \
    --opt build-arg:name=my-app \
```

## output
```sh
--output type=image,name=docker.io/username/image,push=true
```

have multiple tags: https://stackoverflow.com/questions/58691068/buildctl-command-to-tag-multiple-images
```sh
buildctl build \
  --frontend dockerfile.v0 \
  --local context=. \
  --local dockerfile=. \
  --output type=image,\"name=test/repo:tag1,test/repo:tag2\",push=true
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
