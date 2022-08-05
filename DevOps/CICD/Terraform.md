# Terraform

## install
Windows: 
- download the exe and extract it into a folder
- add the folder path to the `path` env
- `terraform -version`

## terragrunt
https://repo1.dso.mil/platform-one/big-bang/customers/template/-/tree/main/terraform
```
terragrunt run-all init    #initialize
terragrunt run-all plan    #pre-check 
terragrunt run-all apply   #deploy, this incurs cost!
terragrunt run-all destroy #destroy
terragrunt run-all show -json planfile
```
