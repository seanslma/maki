# Buildkit

## docs
https://docs.docker.com/build/buildkit/

## how it works
https://depot.dev/blog/buildkit-in-depth
- buildkit coverts everything from frontends and backends to LLB (low-level build) and DAGs (directed acyclic graphs)
- to take advantage of parallelization, must rewrite Dockerfile to use multi-stage builds.

## extract info
```sh
buildctl --version      # get buildkit version
buildctl --frontend dockerfile.v0 --opt export=true --local . # get active builders
buildctl debug labels
```

## build command and parameters
