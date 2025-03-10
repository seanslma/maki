# Buildkit

## disk usage
https://github.com/moby/buildkit/issues/4218

check where disk has been used and the solution!!!

run into the buildkitd pod:
```sh
du -sh
```

## docs
https://docs.docker.com/build/buildkit/

## how it works
https://depot.dev/blog/buildkit-in-depth
- buildkit coverts everything from frontends and backends to LLB (low-level build) and DAGs (directed acyclic graphs)
- to take advantage of parallelization, must rewrite Dockerfile to use multi-stage builds.

## k8s example
https://kubernetes.courselabs.co/labs/buildkit/

## deploy example
https://medium.com/@t-velmachos/build-docker-images-on-k8s-faster-with-buildkit-3443e36aef2e

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
---
      containers:
      - name: buildkitd
        image: moby/buildkit:v0.9.0
        args:
          - --addr
          - unix:///run/buildkit/buildkitd.sock
          - --addr
          - tcp://0.0.0.0:1234
          - --config=/home/user/.config/buildkit/buildkitd.toml
        securityContext:
          privileged: true #cannot be false
        ports:
          - name: buildkitd
            containerPort: 1234
        volumeMounts:
        - name: buildkitd-config
          mountPath: /home/user/.config/buildkit
      volumes:
      - name: buildkitd-config
        configMap:
          name: buildkitd
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

## why there is no `metadata.json`
when set `--metadata-file metadata.json` after build I cannot find the json file. reason: the json file will be created only if you set `--output`

## authorization
```
failed to authorize:
failed to fetch anonymous token:
unexpected status from GET request to
https://my_acr.azurecr.io/oauth2/token?scope=repository%3Adev%2Ftest%3Apull%2Cpush&service=my_acr.azurecr.io:
401 Unauthorized
```
https://github.com/moby/buildkit/issues/2136
- The docker registry credentials should be on the `buildctl` client side, not on the buildkit daemon
