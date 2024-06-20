# Docker

## self-hosted tfs agent
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
- https://github.com/Azure/AKS/issues/2343
- docker build will not function as of aks 1.19 as the container runtime changed from `docker` to `containerd` on AKS
- alternatives: https://docs.microsoft.com/en-us/azure/aks/cluster-configuration#container-runtime-configuration

## use `buildkit` in aks
https://medium.com/@aabeing/aks-as-azure-devops-agents-buildkit-5af8e5cd43d1
- create a `buildkit` server
- install `buildctl` in self-hosted tfs agent
- use `podman` / `buidah`: https://www.reddit.com/r/azuredevops/comments/o5noa8/how_to_build_container_images_from_selfhosted/

## can we use `podman`
https://medium.com/@reachpankajdhami/running-azure-devops-self-hosted-agent-on-aks-for-building-docker-images-with-podman-2fa052e6409d
