# Auth

## Kubernetes client API error 401 - Unauthorized
add configuration to cluster config
```
kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts
```
