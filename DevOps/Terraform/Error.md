# Error

## Error while retrieving OAuth token: Code Expired
https://github.com/hashicorp/terraform-provider-kubernetes/issues/606
Possible solutions
- fetch the AKS credentials before run terraform and then try any kubectl cmd. This way you will manage to auth.
- when fetch credentials for AKS, fetch the admin ones(param --admin). The admin account does not need to register, or at least in my case.
