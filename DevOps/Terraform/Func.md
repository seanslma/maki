# Func

## yamldecode
https://developer.hashicorp.com/terraform/language/functions/yamldecode

Get value from yaml file
```
module "example" {
  source = "../modules/example"
  value = yamldecode(file("${path.module}/example.yaml")).configs.value
}

output "example_value" {
  value = jsondecode(helm_release.argocd.metadata[0].values).configs.value
}
```
