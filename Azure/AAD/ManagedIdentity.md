# Managed Identity
https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview

- Managed identities provide an automatically managed identity in Azure Active Directory for applications to use when connecting to resources that support Azure Active Directory (Azure AD) authentication.
- Applications can use managed identities to obtain Azure AD tokens without having to manage any credentials.
- Two types: `System assigned` (1:1) and `User assigned` (1:n)
- The key difference between Azure managed identities and service principals is that, with the former, admins do not have to manage credentials, including passwords.

## benifit
https://learningbydoing.cloud/blog/stop-using-client-secrets-start-using-managed-identities/

## Managed identity for container
https://learn.microsoft.com/en-us/azure/container-instances/container-instances-managed-identity

## show the added pod-identity
```
kubectl get azureidentity
```

## add manged identity to aks
```
az aks pod-identity add --resource-group <rg-name> \
  --cluster-name <cluster-name> --namespace <namespace> \
  --name csi-to-key-vault --identity-resource-id <managed-identity-resource-id>
```
