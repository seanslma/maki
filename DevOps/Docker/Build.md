# Build

## command output from dockerfile
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
