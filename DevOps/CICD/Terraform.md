# Terraform

https://repo1.dso.mil/platform-one/big-bang/customers/template/-/tree/main/terraform

terragrunt run-all init    #initialize
terragrunt run-all plan    #pre-check 
terragrunt run-all apply   #deploy, this incurs cost!
terragrunt run-all destroy #destroy
terragrunt run-all show -json planfile
