# Build

## build image
```sh
docker build https://github.com/docker/rootfs.git#<container-branch>:<docker-dir>
docker build . -f ./docker/filepath/my.docker --platform linux/amd64 -t 1.0.0 -t latest #manually build locally
```
Note that the `dot` is the context. When doing a docker build, 
- the files from your local context are sent to the daemon, and put in a temporary directory;
- that temporal directory is used to build the image (the actual build is performed on the daemon side).

## multistage build
https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/

## COPY failed: stat /var/lib/docker/tmp/docker-builder<number>/xxxx no such file or directory
- the current context is not correct
- the directory was in `.dockerignore` file so it was not copied to the builder folder
