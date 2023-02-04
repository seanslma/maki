# Terragrunt

https://repo1.dso.mil/platform-one/big-bang/customers/template/-/tree/main/terraform

https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/

- make providers dry
- make backend dry
- will automatically determine dependencies

## install in linux from binary
find the latest in the assets section in: https://github.com/gruntwork-io/terragrunt/releases
```
wget https://github.com/gruntwork-io/terragrunt/releases/download/v0.42.5/terragrunt_linux_amd64
mv terragrunt_linux_amd64 terragrunt
chmod u+x terragrunt
sudo mv terragrunt /usr/local/bin/terragrunt
terragrunt --help
```

## commands
```
terragrunt run-all init    #initialize
terragrunt run-all plan    #pre-check
terragrunt run-all plan *> c:/terragrunt.plan.output #had issues
terragrunt run-all apply   #deploy, this incurs cost!
terragrunt run-all destroy #destroy
terragrunt run-all show -json planfile
```

## execute terraform command on specific module
- cd into that module and run command without run-all, or
- use `--terragrunt-working-dir <module-path>` parameter

## hcl
root
- remote_state
- generate "provider"

subfolder
- include
- dependency
- inputs

## provider
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

## backend

## dependency
terragrunt.hcl
```
dependency "aks" {
  config_path = "../aks"
  mock_outputs = {
    cluster_name           = "mock-name"
    cluster_resource_group = "mock-rg"
  }
}

inputs = {
  aks_name           = dependency.aks.cluster_name
  aks_resource_group = dependency.aks.cluster_resource_group
}
```

## inputs
get the dependency outputs as inputs of the variables in the current module
