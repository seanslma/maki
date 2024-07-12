# aad_pod_identity

https://azure.github.io/aad-pod-identity/docs/getting-started/installation/#quick-install

https://azure.github.io/aad-pod-identity/docs/demo/standard_walkthrough/

https://learn.microsoft.com/en-us/azure/aks/use-azure-ad-pod-identity

## depreciated
https://github.com/Azure/aad-pod-identity

New one to use `Azure Workload Identity`: https://azure.github.io/azure-workload-identity/docs

## `AzureIdentity` vs `ClusterRole`
**AzureIdentityBinding** is specific to AKS and is part of the Azure AD Pod Identity (AAD Pod Identity) feature:
- Enables secure access to Azure resources from within Kubernetes pods using Azure identities.

**ClusterRoleBinding** is a Kubernetes resource used to bind a Role or ClusterRole to a user, group, or service account within a namespace, specifying the permissions they have:
- Defines access within the Kubernetes cluster, such as the ability to list, get, or watch specific resources (pods, services, etc.).

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
```sh
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
