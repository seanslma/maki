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

## using k8s internal url
```sh
./buildctl --addr tcp://buildkitd:1234 build \
--frontend=dockerfile.v0 \
--local context=. \
--local dockerfile=./linux/ \
--opt filename=my-app.docker \
--output type=image,name=<registry-service-name>.<namespace>.svc.cluster.local:5000/dev/test,push=true,registry.insecure=true
```

## local registry using http
https://stackoverflow.com/questions/75192693/how-to-use-buildctl-with-localhost-registry-with-tls

remote error: `tls: unrecognized name`
```sh
buildctl build \
--frontend=dockerfile.v0 \
--local context=. \
--local dockerfile=. \
--output type=image,name=192.168.0.110:8082/docker-local/test,push=true,registry.insecure=true \
--export-cache type=registry,ref=192.168.0.110:8082/docker-local/test,mode=max,push=true,registry.insecure=true \
--import-cache type=registry,ref=192.168.0.110:8082/docker-local/test,registry.insecure=true 
```

The buildkit daemon needs to be run with a configuration file that specifies the registry is `http` instead of `https`. 
See the documentation on buildkitd.toml: https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md
```toml
[registry."192.168.0.110:8082"]
  http = true
  insecure = true #required?
```
The file path is 
- rootful mode: `/etc/buildkit/buildkitd.toml`
- rootless mode: `~/.config/buildkit/buildkitd.toml`

## workaround for dockerfile from http registry
https://github.com/moby/buildkit/issues/2044

Use Secret or ConfigMap to mount the config file: 
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: buildkit
  namespace: buildkit
data:
  buildkitd.toml: |
    debug = false
    [worker.containerd]
      namespace = "buildkit"
    [registry."registry:5000"]
      http = true
      insecure = true
```

Worked solution:
If you are building on top of the job.rootless.yaml template
then you can add `--config /etc/buildkit/buildkitd.toml`
in https://github.com/moby/buildkit/blob/master/examples/kubernetes/job.rootless.yaml#L31-L32

## self-signed vertificate
https://github.com/moby/buildkit/issues/4149
- install the self-signed certificates on the machine
- maybe also works for installing the certs in the buildkit docker image
- if the registry in the same kubernetes cluster, using internal url

https://docs.docker.com/build/buildkit/configure/#setting-registry-certificates
- set self-signed registry certificate

## failed to do request `i/o timeout`
https://github.com/docker/buildx/issues/191
- used the wrong url for the registry
- did not include the port when using internal url
