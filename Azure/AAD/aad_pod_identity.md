# aad_pod_identity

https://azure.github.io/aad-pod-identity/docs/getting-started/installation/#quick-install

https://azure.github.io/aad-pod-identity/docs/demo/standard_walkthrough/

https://learn.microsoft.com/en-us/azure/aks/use-azure-ad-pod-identity

## create `AzureIdentity` and `AzureIdentityBinding`
```yaml
apiVersion: "aadpodidentity.k8s.io/v1"
kind: AzureIdentity
metadata:
  name: "{{ .Values.azureIdentity.name }}"
  namespace: "{{ .Values.namespace }}"
spec:
  type: 0
  resourceID: "{{ .Values.azureIdentity.resourceID }}"
  clientID: "{{ .Values.azureIdentity.clientID }}"
---
apiVersion: "aadpodidentity.k8s.io/v1"
kind: AzureIdentityBinding
metadata:
  name: "{{ .Values.azureIdentity.name }}"
  namespace: "{{ .Values.namespace }}"
spec:
  azureIdentity: "{{ .Values.azureIdentity.name }}"
  selector: "{{ .Values.azureIdentity.name }}"
```

## reference the created AzureIdentity
AAD Pod Identity enables Kubernetes applications to access cloud resources securely with Azure Active Directory.
```yaml
metadata:
  name: demo
  labels:
    app: "{{ .Chart.Name }}"
    aadpodidbinding: "{{ .Values.azureIdentity.name }}"    
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
