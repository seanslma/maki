# Buildctl
https://github.com/moby/buildkit/blob/master/docs/reference/buildctl.md
```sh
buildctl [global options] command [command options] [arguments...]
```

https://github.com/moby/buildkit#imageregistry

## transition from docker to buildkit
https://dille.name/slides/2020-05-28/110_ecosystem/buildkit/transition.final/

example
```sh
docker build \
    . -f ./docker/linux/my-app.docker \
    --build-arg NAME=my-app \
    --no-cache --force-rm \
    -t docker.example.com/uat/my-app:0.1.0

buildctl build \
    --frontend dockerfile.v0 \
    --local context=. \
    --local dockerfile=./docker/linux/ \ # can only be a directory
    --opt filename=my-app.docker \       # the dockerfile name
    --opt build-arg:NAME=my-app \  
    --opt no-cache=true   
    --output type=image,name=docker.example.com/uat/my-app:0.1.0
```

Note that the `NAME` is a variable define in dockerfile `IMAGE_NAME=${NAME}`.

## buildkitd address
Global option. Default: `unix:///run/buildkit/buildkitd.sock`
```sh
--addr tcp://buildkitd:1234
```

## deploy buildkit in kubernetes
https://kubernetes.courselabs.co/labs/buildkit/
- deploy `buildkitd`
- deploy agent pod with `buildctl`
- test build with a dummy dockerfile

```sh
# install wget
sudo apt update && sudo apt install wget

# install buildkit release
wget https://github.com/moby/buildkit/releases/download/v0.15.2/buildkit-v0.15.2.linux-amd64.tar.gz
tar xvf buildkit-v0.15.2.linux-amd64.tar.gz

# download a dockerfile
cd bin
wget --no-check-certificate https://raw.githubusercontent.com/courselabs/kubernetes/main/labs/docker/simple/Dockerfile
mkdir linux
mv ./Dockerfile ./linux/my-app.docker
cat ./linux/my-app.docker

# build the image
./buildctl --addr tcp://buildkitd:1234 build --frontend=dockerfile.v0 --local context=. --local dockerfile=./linux/ --opt filename=my-app.docker --output type=image,name=docker.example.com/dev/test,push=true
```

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
# to local folder
--output type=local,dest=path/to/output-dir
# to registry
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
# export cache to local directory
--export-cache type=local
# use azure blob storage
--import-cache type=azblob,account_url=https://myaccount.blob.core.windows.net,name=my_image \  
--export-cache type=azblob,account_url=https://myaccount.blob.core.windows.net,name=my_image \
```

## metadata to file
will write `metadata.json` only when `--output` is set.
```sh
--metadata-file metadata.json
```

cat metadata.json
```json
{
  "containerimage.config.digest": "sha256:bf6010de5e36c4a6d2cefd562e65d25b8713c36575",
  "containerimage.descriptor": {
    "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
    "digest": "sha256:09423f01912c6cacd4363ac24bfd90760ce52606e8c71cf4f",
    "size": 891,
    "platform": {
      "architecture": "amd64",
      "os": "linux"
    }
  },
  "containerimage.digest": "sha256:09423f01912c6cacd4363ac24bfd90760ce52606e8c71cf4f",
  "image.name": "docker.example.com/dev/test"
}
```
