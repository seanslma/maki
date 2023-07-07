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
To add a role assignment in Azure for a user-created system-managed identity with a scope for a blob storage container, 
you can follow these steps:
- Identify the system-managed identity you want to assign the role to. If you haven't created one yet, you can create a system-managed identity in Azure by going to the Azure portal, navigating to the appropriate resource (such as a virtual machine or an Azure Function), and enabling the system-managed identity feature.
- Once you have the system-managed identity created, note down its client ID or object ID. You will need this identifier in the next steps.
- Navigate to the Azure portal and open the Azure Storage account containing the blob storage container.
- Inside the storage account, go to the "Access control (IAM)" tab. Click on the "Add role assignment" button to create a new role assignment.
  - In the "Add role assignment" dialog, select the appropriate role you want to assign. For example, if you want to grant the identity read access to the blob storage container, you can choose the "Storage Blob Data Reader" role.
  - In the "Assign access to" field, search for and select the system-managed identity you identified earlier. You can search for the identity using its client ID or object ID.
  - In the "Scope" field, enter the scope for the role assignment. In this case, you should enter the resource ID of the blob storage container you want to grant access to. The resource ID should have the following format:
```
/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers \ 
    /Microsoft.Storage/storageAccounts/{storageAccountName}/blobServices/default/containers/{containerName}
```
- Click on the "Save" button to create the role assignment.

The system-managed identity should now have the assigned role with the specified scope for the blob storage container. It will be able to access the container according to the permissions granted by the assigned role.
