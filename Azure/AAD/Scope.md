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

add storage account  
```
az role assignment create \
  --assignee <identity-principal-id> \
  --role 'Storage Blob Data Contributor' \
  --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group> \
    /providers/Microsoft.Storage/storageAccounts/<storage-acctount>
```
add blob storage container
```
az role assignment create \
  --role "Storage Blob Data Contributor" \
  --assignee <email> \
  --scope "/subscriptions/<subscription_id>/resourceGroups/<resource-group> \
    /providers/Microsoft.Storage/storageAccounts/<storage-account>/blobServices/default/containers/<container>"
```

The system-managed identity should now have the assigned role with the specified scope for the blob storage container. It will be able to access the container according to the permissions granted by the assigned role.

## .default scope
https://dev.to/425show/just-what-is-the-default-scope-in-the-microsoft-identity-platform-azure-ad-2o4d
```
https://graph.microsoft.com/Mail.Read
https://graph.microsoft.com/User.Read
```

The `/.default` scope is a shortcut back to the Azure AD v1 behavior (e.g., static consent).
There are two extra scenarios where the `/.default` scope is required (`https: //your-app.your-co.com/.default`): 
- `client_credentials`: our app is making service-to-service calls or using application-only permissions (also known as application app roles in Azure AD parlance), or
- when using the `on-behalf-of` (OBO) flow, where our API is making calls on behalf of the user to a different API; something like this: client app --> our API --> Graph API.
