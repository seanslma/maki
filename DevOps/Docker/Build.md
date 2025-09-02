# Build

- build context
- pass value to ARG: `--build-arg NAME=my-app`

## simple docker test
```dockerfile
FROM alpine

ARG BASE_URL=https://example.com
ARG FILE_URL=${BASE_URL}/file.txt

RUN echo "Downloading from: ${FILE_URL}"
```
Then run it `docker build -f ./test.docker -t test .`

## build an image
```sh
docker build https://github.com/dev/test.git#<branch>:<docker-dir>
docker build . --no-cache --force-rm -t docker.example.com/image-name:linux
docker build . -f ./docker/linux/my-dev.docker --platform linux/amd64 -t 1.0.1
```
- `--no-cached`: do not use cached intermediate layers and regenerate them as well
- `--rm`: remove intermediate containers after a successful build
- `--force-rm`: those intermediate containers would always been removed even in case of an unsuccessful compilation
- `-t --tag`: name and optionally a tag in the `name:tag` format

Note that the `dot` is the context. When doing a docker build,
- the files from your local context are sent to the daemon, and put in a temporary directory;
- that temporal directory is used to build the image (the actual build is performed on the daemon side).
- paths in a Dockerfile are always relative to the the context directory

## multistage build
Multi-stage build is a feature introduced in Docker 17.05. Multistage build can reduce docker image size.
- https://collabnix.com/getting-started-with-docker-multi-stage-builds/
- https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/


## COPY failed: stat /var/lib/docker/tmp/docker-builder<number>/xxxx no such file or directory
- the current context is not correct
- the directory not in the current context folder
- the directory was in `.dockerignore` file so it was not copied to the builder folder
- the docker daemon doesn't have sufficient rights or space to create the temporary directory and files
- there's a bug in the directive that fails to place the expected files from 'current context' to into the temporary directory

## how to show the created date of the based image in dockerfile?

## command output from dockerfile
cat output will show in the output
```dockerfile
RUN openssl s_client -connect www.example.com:443 &> log_openssl.txt; cat log_openssl.txt
```

## enable command output
will also force not using cache
```sh
docker build --progress=plain --no-cache
```
or set
```sh
DOCKER_BUILDKIT=0 docker build ...
```
