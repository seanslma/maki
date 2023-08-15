# Import Existing Resources

https://dev.to/cloudskills/getting-started-with-terraform-on-azure-importing-existing-infrastructure-43fa

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
