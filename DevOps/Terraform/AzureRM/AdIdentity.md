# AdIdentity

## access to blob storage
https://stackoverflow.com/questions/52769758/azure-blob-storage-authorization-permission-mismatch-error-for-get-request-wit

For blob storage, to let an app to access a specific blob container,
we have to include that blob container in the `azurerm_role_assignment` scope for that app.

```tf
# https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_assignment
resource "azurerm_role_assignment" "blob_contributor" {
  # https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor
  scope                = var.st_blob.container["dev-data"].resource_manager_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = module.ad_identity.principal_id
}

# https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_assignment
resource "azurerm_role_assignment" "queue_contributor" {
  # https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor
  scope                = var.st_blob.container["dev-data"].resource_manager_id
  role_definition_name = "Storage Queue Data Contributor"
  principal_id         = module.ad_identity.principal_id
}
```

