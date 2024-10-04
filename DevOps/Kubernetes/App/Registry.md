# Registry

## kubelet pull images from internal registry using local url not possible
- https://github.com/k3s-io/k3s/issues/1581
- Containerd runs containers for the Kubelet, but runs on the host and is not itself part of the cluster nor aware of its existence.
- If the host you're running K3s on cannot resolve in-cluster DNS names, then neither can containerd.
- hack: use `NodePort` - expose static port to k8s node: https://medium.com/@lumontec/running-container-registries-inside-k8s-6564aed42b3a

