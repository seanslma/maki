# Terraform

learn:
https://learnk8s.io/terraform-aks

https://www.linkedin.com/pulse/one-hour-day-learn-terraform-microsoft-azure-gary-tong

## blogs
https://blog.gruntwork.io/a-comprehensive-guide-to-terraform-b3d32832baca

https://blog.gruntwork.io/terraform-tips-tricks-loops-if-statements-and-gotchas-f739bbae55f9

## scheduled maintenance
See: https://status.hashicorp.com/

## basic
```
terraform init
terraform plan -out main.tfplan
terraform apply main.tfplan
echo "$(terraform output resource_group_name)" #check the name from the outputs
terraform plan -destroy -out main.destroy.tfplan
terraform destroy
```

## update
- update terraform states to match current state of the actual resources: `terraform refresh`
- add manually created resource under source control: `terraform import`

## best practices
https://cloud.google.com/docs/terraform/best-practices-for-terraform#module-structure

environment directory must contain:
- `main.tf`: instantiate the service module
- `backend.tf`: declare the Terraform backend state location (typically, Cloud Storage)

module directory should contain:
- `main.tf`
- `variables.tf`
- `outputs.tf`
