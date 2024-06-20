# Docker

## self-hosted tfs agent
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
- https://github.com/Azure/AKS/issues/2343
- docker build will not function as of aks 1.19 as the container runtime changed from `docker` to `containerd` on AKS
- alternatives: https://docs.microsoft.com/en-us/azure/aks/cluster-configuration#container-runtime-configuration

## alternative as `containerd` replaced `docker` in aks
https://juejin.cn/post/6943558078269030408

### use `docker buildx` in aks
https://medium.com/@aabeing/aks-as-azure-devops-agents-buildkit-5af8e5cd43d1
- details for the deployment of the buildkit in aks

https://techblog.greeneye.ag/blog/kubernetes-continuous-integration-using-buildkit-buildx-and-docker-regisrty
- details to describe how to choose the tools for migrating from aks docker to buildkit
- also mentioned tech details duch cache etc

How to do it:
- create a `buildkit` server
- install `buildctl` in self-hosted tfs agent
- use `podman` / `buidah`:
  - https://www.reddit.com/r/azuredevops/comments/o5noa8/how_to_build_container_images_from_selfhosted/
  - https://medium.com/@reachpankajdhami/running-azure-devops-self-hosted-agent-on-aks-for-building-docker-images-with-podman-2fa052e6409d

```sh
docker buildx create --driver kubernetes --driver-opt replicas=3 --use
docker buildx build -t example.com/foo --push .
```

buildkit:
https://www.sliceofexperiments.com/p/a-comprehensive-guide-for-the-fastest

### use `buildah` in aks
```sh
# build docker image
buildah bud -t example.com/foo:latest .
# list docker images
buildah images
```

### kaniko
- slow?
