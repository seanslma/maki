# Image Build

## build image
```
docker build https://github.com/docker/rootfs.git#<container-branch>:<docker-dir>
docker build . -f ./docker/filepath/my.docker --platform linux/amd64 -t 1.0.0 -t latest #manually build locally
```

## multistage build
https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/
