# provider
```
# root folder
generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite"
  contents  = <<EOF
    terraform {
      required_providers {
        azurerm = {
          source  = "hashicorp/azurerm"
          version = "3.0.0"
        }
      }
      #backend "azurerm" {}
    }

    provider "azurerm" {
      features {}
      subscription_id = "2445bc57-cb0e-448a-ac3a-c4c41c63eef2"
    }
 }

# moduler terragrunt.hcl
include {
  path = find_in_parent_folders()
}
```
