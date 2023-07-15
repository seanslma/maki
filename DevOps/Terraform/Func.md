# Func

## yamldecode
https://developer.hashicorp.com/terraform/language/functions/yamldecode

Get value from yaml file
```tf
module "example" {
  source = "../modules/example"
  value = yamldecode(file("${path.module}/example.yaml")).configs.value
}

output "example_value" {
  value = jsondecode(helm_release.argocd.metadata[0].values).configs.value
}
```

## replace
replace user/pass url to ssh url:
```tf
replace(yamldecode(helm_release.argocd.metadata[0].values).configs.repo_url, "https://github.com/", "git@github.com:")
```
