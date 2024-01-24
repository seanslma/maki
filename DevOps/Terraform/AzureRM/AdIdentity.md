# AdIdentity

## Relationship between `AzureIdentity` in helm and `azurerm_user_assigned_identity` in terraform
**AzureIdentity (Helm)**
- **Purpose:** A configuration parameter within the Azure AD Pod Identity (AAD Pod Identity) Helm chart.
- **Function:** It enables pods in a Kubernetes cluster to access Azure resources using a managed identity.
- **Configuration:** It's defined within the `values.yaml` file of the AAD Pod Identity chart.
- **Key Properties:**
    - `resourceID`: The ID of the user-assigned managed identity.
    - `clientID`: The client ID of the managed identity.
    - `name`: A name for the identity within the namespace.
    - `namespace`: The namespace where the identity is created.

**azurerm_user_assigned_identity (Terraform)**
- **Purpose:** A Terraform resource that creates and manages user-assigned managed identities in Azure.
- **Function:** It provides a way to create and manage these identities independently of other resources.
- **Configuration:** It's defined in Terraform configuration files using the `azurerm_user_assigned_identity` resource.
- **Key Properties:**
    - `name`: The name of the managed identity.
    - `resource_group_name`: The resource group where the identity is created.
    - `location`: The Azure region where the identity is created.

**Relationship**
- **Integration:** They work together to enable pods in a Kubernetes cluster to access Azure resources using managed identities:
    1. **Terraform:** Creates the user-assigned managed identity using `azurerm_user_assigned_identity`.
    2. **Helm:** Refers to the created managed identity using `AzureIdentity` within the AAD Pod Identity chart.
- **Coordination:** Terraform generates the necessary information (resource ID, client ID) for the `AzureIdentity` configuration in Helm.

**Terraform code:**
```terraform
resource "azurerm_user_assigned_identity" "my_identity" {
  name                = "my-identity"
  resource_group_name = "my-resource-group"
  location            = "eastus"
}
```

**Helm values.yaml:**
```yaml
azureIdentities:
  - name: "my-identity"
    resourceID: "${azurerm_user_assigned_identity.my_identity.id}"
    clientID: "${azurerm_user_assigned_identity.my_identity.client_id}"
    # ... other configuration
```

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

