# Storage
- azurerm_storage_container
- stoarge_account_network_rules
- azurerm_storage_container
- azurerm_private_endpoint: dfs, file, blob

## Add a manully created azure blob storage container under terraform control
We can manage an existing Azure Blob Storage container using Terraform. 
Terraform has an Azure provider that allows you to define and manage Azure resources, including Blob Storage containers.

To manage an existing Blob Storage container in Terraform, wed need to `import` it into the Terraform state. 
The import process enables Terraform to track the existing resource and manage its state going forward. 

Here's how we can do it:

1. Create a new Terraform configuration file or update an existing one to include the Azure provider and the Blob Storage container resource definition. 
```tf
provider "azurerm" {
  features {}
}

resource "azurerm_storage_container" "example" {
  name                  = "<container-name>"
  storage_account_name  = "<storage-account-name>"
  resource_group_name   = "<resource-group-name>"
  container_access_type = "private"
}
```

2. Replace `<container-name>`, `<storage-account-name>`, and `<resource-group-name>` with the actual names of the 
Blob Storage container, storage account, and resource group.
- Run terraform init to initialize the Terraform configuration.
- Run the import command to import the existing Blob Storage container into the Terraform state:
```sh
terraform import azurerm_storage_container.example \
  /subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers \
  /Microsoft.Storage/storageAccounts/<storage-account-name>/blobServices/default/containers/<container-name>
```

3. Replace `<subscription-id>`, `<resource-group-name>`, `<storage-account-name>`, and `<container-name>` with the respective values for the Blob Storage container.
- Run terraform plan to verify the import was successful and to see any changes that Terraform would apply.
- Finally, run terraform apply to apply the changes and manage the Blob Storage container through Terraform.

Note that importing an existing resource does not delete or modify the resource itself. 
Terraform tracks the resource's state and can manage it going forward. 
Therefore, your data in the Blob Storage container will not be lost during this process.

However, exercise caution when applying changes to the Terraform configuration that manages the Blob Storage container, 
as inappropriate modifications can result in unintended consequences. 
Always review the Terraform plan before applying changes to ensure they align with your expectations and requirements.

## azurerm_storage_container
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_container

## stoarge_account_network_rules
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account_network_rules

when nfsv3_enabled = true, network_rules must be created together with the storage.
see bug: https://github.com/hashicorp/terraform-provider-azurerm/issues/14540

```tf
resource "azurerm_storage_account_network_rules" "main" {
  storage_account_id         = azurerm_storage_account.main.id
  default_action             = "Deny"
  ip_rules                   = ["127.0.0.1"]
  virtual_network_subnet_ids = [azurerm_subnet.main.id]
  bypass                     = ["Metrics"]
}
```

## azurerm_private_endpoint
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/private_endpoint
- subresource_names: dfs - general file system access
- subresource_names: file - only for FileStorage
- subresource_names: blob - for type != FileStorage
