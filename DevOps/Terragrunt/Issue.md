# Issue

## checksums mismatch
Updating terraform version will get error `Terraform does not match any of the checksums recorded in the dependency lock file`.

Solution:
- Delete all `.terraform.lock.hcl` files: `Get-ChildItem -Path . -Filter ".terraform.lock.hcl" -Recurse | Remove-Item -Force`
- Delete all `.terraform` folders: `Get-ChildItem -Path . -Filter ".terraform" -Directory -Recurse -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force`
- Run `terragrunt run-all init -upgrade`
