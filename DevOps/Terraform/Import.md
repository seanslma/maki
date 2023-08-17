# Import Existing Resources

https://dev.to/cloudskills/getting-started-with-terraform-on-azure-importing-existing-infrastructure-43fa

- Import manully created resources to be under the control of terraform configurations. 
- Manage pre-existing infrastructure by terraform

## simple resource
- create terraform code
- import state: `terraform init` and `terraform import <terraform-resource-name>.<resource-label> <azure-resource-id>`
- check new resource in state file: `cat terraform.tfstate`
- validate terraform configuration `terraform plan` should report no chnages

## multiple resources
- create terraform code for all resources
- import state for resources one by one
- check and validate the states

## import module
- in module folder run `terraform init`
- then for each resource run `terraform import module.<module-name>.<terraform-resource-name>.<resource-label> <azure-resource-id`

## import one of for_each
in unix shell, use single quotes to make the inner address be taken literally
```sh
terraform import 'module.my_storage_account.azurerm_storage_container.container["my-data"]' foo
```
in windows the double quotes must be escaped with a backslash:
```sh
terraform import module.my_storage_account.azurerm_storage_container.container[\"my-data\"] foo
```

## import with variables
https://stackoverflow.com/questions/57187782/how-to-use-terraform-import-with-passed-in-variables
```sh
terraform import -var 'environment=sandbox' azurerm_storage_account.my_storage foo
terraform import -var-file='../tfvars/prod.tfvars' 'module.MySystem.azurerm_windows_virtual_machine.windsvm["dsvm0003"]' "/subscriptions/xxx-xxx-xxx-xxx-xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/DSVM0003"
```
