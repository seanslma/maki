# Certificate

## error using `kubectl`
```
Unable to connect to the server:
tls: failed to verify certificate: x509: certificate has expired or is not yet valid:
current time 2024-10-29T11:52:50+10:00 is after 2023-10-20T00:44:13Z
```
Can access the aks cluster from other machines.
Solution: Updated firewall rules and it worked.

## check expiration
https://github.com/Azure/AKS/issues/2347

## check serving-cert
```sh
kubectl get secrets serving-cert -n kube-system -o yaml
```

## rotate certificate
- https://stackoverflow.com/questions/65219904/kubernetes-azures-aks-suddenly-gives-error-kubectl-x509-certificate-has-expi
- https://learn.microsoft.com/en-us/azure/aks/certificate-rotation

manual certificate rotation
```sh
az aks rotate-certs -g $RESOURCE_GROUP_NAME -n $CLUSTER_NAME
az aks get-credentials -g $RESOURCE_GROUP_NAME -n $CLUSTER_NAME --overwrite-existing
```
