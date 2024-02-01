# Error

## Error while retrieving OAuth token: Code Expired
https://github.com/hashicorp/terraform-provider-kubernetes/issues/606
Possible solutions
- fetch the AKS credentials before run terraform and then try any kubectl cmd. This way you will manage to auth.
- when fetch credentials for AKS, fetch the admin ones(param --admin). The admin account does not need to register, or at least in my case.
- switch to root before run terraform `sudo -i`
- my solution: do not run `az login` in vscode terminal - has restricted permisison, run it in a standard terminal

```
az account get-access-token
az login --tenant <my-tenantid>
```


## Invalid value for "path" parameter: no file exists at "values.yaml"
https://stackoverflow.com/questions/62127753/why-do-i-get-call-to-function-file-failed-no-file-exists
```
values = [
    file("values.yaml")
]
```
When referring to a file in the calling module from a child module, an absolute path based on the calling module's path using `path.module` should be provided:
```
module "dev" {
    source = "../modules/dev"
    values_path = "${path.module}/values.yaml"
}
```
Another solution: provide the entire file as a variable (this is what the `file` function does):
```
module "dev" {
    source = "../modules/dev"
    values = file("${path.module}/values.yaml")
}
```

## Failed to construct REST client
https://github.com/hashicorp/terraform-provider-kubernetes/issues/1775

The kubernetes_manifest resource needs access to the API server of the cluster during planning (cluster must exist).

This is because, in order to support CRDs in Terraform ecosystem, we need to pull the schema information for each manifest resource at runtime (during planing).

## Error: `Backend configuration changed`
The `.terraform` folder or the cache must be cleared.
