# Docker

# self-hosted tfs agent
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
- https://github.com/Azure/AKS/issues/2343
- docker build will not function as of aks 1.19 as the container runtime changed to containerd on AKS
- alternatives: https://docs.microsoft.com/en-us/azure/aks/cluster-configuration#container-runtime-configuration
