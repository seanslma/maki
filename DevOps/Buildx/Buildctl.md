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
- deploy `buildkitd`
- deploy agent pod with `buildctl`
- test build with a dummy dockerfile

```sh
# install wget
sudo apt update && sudo apt install wget

# install buildkit release
wget https://github.com/moby/buildkit/releases/download/v0.9.0/buildkit-v0.9.0.linux-amd64.tar.gz
tar xvf buildkit-v0.9.0.linux-amd64.tar.gz

# download a dockerfile
cd bin
wget --no-check-certificate https://raw.githubusercontent.com/courselabs/kubernetes/main/labs/docker/simple/Dockerfile
mkdir linux
mv ./Dockerfile ./linux/my-app.docker
cat ./linux/my-app.docker

# build the image
./buildctl --addr tcp://buildkitd:1234 build --frontend=dockerfile.v0 --local context=. --local dockerfile=./linux/ --opt filename=my-app.docker --output type=image,name=docker.smc.stanwell.com/dev/test,push=true
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
