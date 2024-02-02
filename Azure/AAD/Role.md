# Role

Roles manage User's access

## check role assignment
```sh
az role assignment list --scope "/subscriptions/<subscription-id>" --role "<role-name>"
az role assignment list --scope "/subscriptions/<subscription-id>" --assignee <user-principal-name-or-object-id>
```

## How to setup the role so the members in a group can have access to the api url?
After creating the `aad group`, `user assigned identity`, and the `role assignment`, 
we should deploy the `AzureIdentity` and `AzureIdentityBinding` in aks so the pod can access the azure resources.

## User Assigned Identity and Role Assignment
In Azure, `azurerm_user_assigned_identity` and `azurerm_role_assignment` are two distinct resources 
that are commonly used together to grant specific roles to a user-assigned managed identity.

The relationship between them is that `azurerm_role_assignment` is used to grant roles to different types of identities
(including user-assigned managed identities created by `azurerm_user_assigned_identity`). 
This allows you to control the permissions and access levels for various resources in your Azure environment. 
The `principal_id` attribute in `azurerm_role_assignment` is typically the identity to which you want to assign a role, 
and this identity can be a user-assigned managed identity among other possibilities.

## **`azurerm_user_assigned_identity`**
- A user-assigned managed identity is an aad identity that can be used to create, manage, and assign to one or more Azure resources.
- is used to create the user-assigned managed identity, and it provides you with an identity that can be assigned roles.
 ```hcl
 resource "azurerm_user_assigned_identity" "example" {
   name                = "your-identity-name"
   resource_group_name = "your-resource-group"
 }
 ```

## **`azurerm_role_assignment`**
- used to assign a role to a user, group, service principal, or managed identity at a specific scope (such as a resource group or resource).
- is often used to grant permissions to the user-assigned managed identity created by `azurerm_user_assigned_identity`.
 ```hcl
 resource "azurerm_role_assignment" "example" {
   principal_id         = azurerm_user_assigned_identity.example.principal_id
   role_definition_name = "Contributor"
   scope                = "/subscriptions/your-subscription-id/resourceGroups/your-resource-group"
 }
 ```
For Key Vault and Blob storage, the role_definition_name and scope are different:
- key vault:
  - `Key Vault Secrets User`
  - `<key_vault>/secrets/<secret>`
- blob storage container:
  - `Storage Blob Data Contributor`
  - `Storage Queue Data Contributor`
  - `storage.container["<name>"].resource_manager_id`

