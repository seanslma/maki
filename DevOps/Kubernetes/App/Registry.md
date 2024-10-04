# Registry

## kubelet pull images from internal registry using local url not possible
- https://github.com/k3s-io/k3s/issues/1581
- Containerd runs containers for the Kubelet, but runs on the host and is not itself part of the cluster nor aware of its existence.
- If the host you're running K3s on cannot resolve in-cluster DNS names, then neither can containerd.
- hack: use `NodePort` - expose static port to k8s node: https://medium.com/@lumontec/running-container-registries-inside-k8s-6564aed42b3a

## local k8s + local registry
https://hackernoon.com/kubernetes-cluster-setup-with-a-local-registry-and-ingress-in-docker-using-kind

# aks + on-prem-registry + self-signed-cert
Add self-signed-cert to the aks nodes:
- https://discuss.kubernetes.io/t/aks-on-prem-registry-self-signed-cert/9308/2
- solution: copy the cert file via a daemonset to the aks nodes
- details: https://github.com/coreos/tectonic-docs/blob/master/Documentation/admin/add-registry-cert.md
- other discussion: https://stackoverflow.com/questions/59723924/azure-kubernetes-service-self-signed-cert-on-private-registry

## delete docker images from registry
https://teplyheng.medium.com/how-to-completely-remove-docker-images-from-a-docker-registry-v2-76d8a26847ff
