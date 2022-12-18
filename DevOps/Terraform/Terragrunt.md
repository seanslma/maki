# Terragrunt

https://repo1.dso.mil/platform-one/big-bang/customers/template/-/tree/main/terraform

https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/

- make providers dry
- make backend dry
- will automatically determine dependencies

## hcl
root
- remote_state
- generate "provider"

subfolder
- include
- dependency
- inputs

## commands
```
terragrunt run-all init    #initialize
terragrunt run-all plan    #pre-check
terragrunt run-all plan *> c:/terragrunt.plan.output #had issues
terragrunt run-all apply   #deploy, this incurs cost!
terragrunt run-all destroy #destroy
terragrunt run-all show -json planfile
```
