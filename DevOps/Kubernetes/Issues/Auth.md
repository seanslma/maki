# Auth

## Kubernetes client API error 401 - Unauthorized
add configuration to cluster config
```
kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts
```

## The connection to the server xx.xx.xx.xx:port was refused - did you specify the right host or port?
Possible reasons
- config not set: `export KUBECONFIG=$HOME/.kube/config`
