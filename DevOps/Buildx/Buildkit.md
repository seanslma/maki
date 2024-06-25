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

## self-signed vertificate
https://github.com/moby/buildkit/issues/4149
- install the self-signed certificates on the machine
- maybe also works for installing the certs in the buildkit docker image
- if the registry in the same kubernetes cluster, using internal url

## failed to do request `i/o timeout`
https://github.com/docker/buildx/issues/191
