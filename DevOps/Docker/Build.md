# Build

## build an image
```
docker build --no-cache --force-rm -t docker.example.com/image-name:linux .
docker build . -f ./docker/linux/my-dev.docker --platform linux/amd64 -t 1.0.1
```

## how to show the created date of the based image in dockerfile?

## command output from dockerfile
cat output will show in the output
```
RUN openssl s_client -connect www.example.com:443 &> log_openssl.txt; cat log_openssl.txt
```

## enable command output
will also force not using cache
```
docker build --progress=plain --no-cache
```

or set
```
DOCKER_BUILDKIT=0 docker build ...
```
