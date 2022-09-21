# ArgoCD

https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops

## Connect to private repo
https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#repositories

https://argo-cd.readthedocs.io/en/release-1.8/user-guide/private-repositories/

Error:
- Unable to deploy revision: rpc error: code = Unknown desc = authentication required

Solution:
- settings > repositories > connecting repo using https > url and pat
