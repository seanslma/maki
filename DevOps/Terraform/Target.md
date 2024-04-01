# Target

## run plan and apply to one resource only
https://spacelift.io/blog/terraform-target

Other unrelevant input variables should be commented out even they are not used!

Assume in the current folder there is a file named `my-module.tf` with 
```tf
module "storage-test" {
  source = "../../modules/module-a"
  ...
}
```
We can run the following `terraform` command to only make changes to this module.
```sh
terraform apply -target module.storage-test
```
