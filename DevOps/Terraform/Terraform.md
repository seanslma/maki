# Terraform

learn:
https://learnk8s.io/terraform-aks

https://www.linkedin.com/pulse/one-hour-day-learn-terraform-microsoft-azure-gary-tong

## scheduled maintenance
See: https://status.hashicorp.com/

## random_id
https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/id


## basic
```
terraform init
terraform plan -out main.tfplan
terraform apply main.tfplan
echo "$(terraform output resource_group_name)" #check the name from the outputs
terraform plan -destroy -out main.destroy.tfplan
terraform destroy
```

## best practices
https://cloud.google.com/docs/terraform/best-practices-for-terraform#module-structure

environment directory must contain:
- `main.tf`: instantiate the service module
- `backend.tf`: declare the Terraform backend state location (typically, Cloud Storage)

module directory should contain:
- `main.tf`
- `variables.tf`
- `outputs.tf`
