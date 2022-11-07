# Terraform

learn:
https://learnk8s.io/terraform-aks

https://www.linkedin.com/pulse/one-hour-day-learn-terraform-microsoft-azure-gary-tong

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
