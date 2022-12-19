# Authorization

https://medium.com/microsoftazure/azure-kubernetes-service-aks-authentication-and-authorization-between-azure-rbac-and-k8s-rbac-eab57ab8345d

## get kubeconfig
```
az aks get-credentials -g <resource-group> -n <cluster-name>
```

## Authentication and Authorization in an AKS cluster
- Authentication using local accounts for both user and admin access / Authorization using Kubernetes RBAC (default)
- Authentication using local accounts for both user and admin access/ no authorization mechanism is enabled
- Authentication using Azure Active directory / Authorization using Kubernetes RBAC only
- Authentication using Azure Active directory / Authorization using both kubernetes RBAC and Azure RBAC (recommended)
