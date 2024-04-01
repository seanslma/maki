# Conditional

## count
A common issue with `count` is that once you delete any resource other than the last one, 
Terraform will try to force replace all resources that the index doesn't match.

Usually **only used for enable/disable a resource**
```tf
variable "add_storage_account" {
  description = "boolean to determine whether to create a storage account or not"
  type        = bool
}

resource "azurerm_storage_account" "main" {
  count = var.add_storage_account ? 1 : 0

  resource_group_name      = "rg-st"
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  name = "stspacelift${count.index}${local.rand_suffix}"
}
```
