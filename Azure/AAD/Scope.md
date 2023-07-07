# Scope

https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview

Scopes manage Application's access. Scope is the set of resources that access applies to. 

## Scope levels
Can specify a scope at four levels: 
- management group
- subscription
- resource group
- resource

## add a role asignment for a scope manually
https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/howto-assign-access-cli

To add a role assignment in Azure for a user-assigned system-managed identity with a scope for a blob storage container, 
you can follow these steps (cannot do it in Azure UI as there is no Scope option):
- Identify the system-managed identity and get the `principal_id`
- run azcli command
```
az role assignment create --assignee <identity_principal_id> --role 'Storage Blob Data Contributor' \
  --scope /subscriptions/<SubscriptionID>/resourceGroups/<ResourceGroup>/providers/Microsoft.Storage/storageAccounts/<StorageAcctount>
```

The system-managed identity should now have the assigned role with the specified scope for the blob storage container. It will be able to access the container according to the permissions granted by the assigned role.
