# Build

## enable command output
will also force not using cache
```
docker build --progress=plain --no-cache
```

or set
```
DOCKER_BUILDKIT=0 docker build ...
```


