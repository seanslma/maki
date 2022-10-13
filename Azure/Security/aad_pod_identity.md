# aad_pod_identity

https://azure.github.io/aad-pod-identity/docs/getting-started/installation/#quick-install

https://azure.github.io/aad-pod-identity/docs/demo/standard_walkthrough/

https://learn.microsoft.com/en-us/azure/aks/use-azure-ad-pod-identity

AAD Pod Identity enables Kubernetes applications to access cloud resources securely with Azure Active Directory.
```
metadata:
  name: demo
  labels:
    aadpodidbinding: $POD_IDENTITY_NAME
```

## list identities
```
az identity list [--resource-group]
az identity create --name --resource-group [--location] [--tags]
az identity delete [--name] [--ids] [--resource-group]
az identity show [--name] [--ids] [--resource-group]
az identity list-operations
az identity list-resources [--filter]
                           [--ids]
                           [--name]
                           [--orderby]
                           [--resource-group]
                           [--skip]
                           [--skiptoken]
                           [--top]
```
