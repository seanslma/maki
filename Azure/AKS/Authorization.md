# Authorization

https://medium.com/microsoftazure/azure-kubernetes-service-aks-authentication-and-authorization-between-azure-rbac-and-k8s-rbac-eab57ab8345d

## Authentication and Authorization in an AKS cluster
- Authentication using local accounts for both user and admin access / Authorization using Kubernetes RBAC (default)
- Authentication using local accounts for both user and admin access/ no authorization mechanism is enabled
- Authentication using Azure Active directory / Authorization using Kubernetes RBAC only
- Authentication using Azure Active directory / Authorization using both kubernetes RBAC and Azure RBAC (recommended)

## get kubeconfig
```
az aks get-credentials -g <resource-group> -n <cluster-name>
```

## install kubelogin
https://github.com/Azure/kubelogin
```
curl -LO https://github.com/Azure/kubelogin/releases/latest/download/kubelogin-linux-amd64.zip
unzip kubelogin-linux-amd64.zip
sudo mv ./bin/linux_amd64/kubelogin /usr/local/bin/

export KUBECONFIG=/path/to/kubeconfig
kubelogin convert-kubeconfig
kubectl get nodes
```
