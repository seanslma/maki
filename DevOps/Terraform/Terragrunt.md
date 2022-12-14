# Terragrunt

https://repo1.dso.mil/platform-one/big-bang/customers/template/-/tree/main/terraform

- will automatically determine dependencies

## commands
```
terragrunt run-all init    #initialize
terragrunt run-all plan    #pre-check
terragrunt run-all plan *> c:/terragrunt.plan.output #had issues
terragrunt run-all apply   #deploy, this incurs cost!
terragrunt run-all destroy #destroy
terragrunt run-all show -json planfile
```
