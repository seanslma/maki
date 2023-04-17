# Private repo

https://levelup.gitconnected.com/connect-argocd-to-your-private-github-repository-493b1483c01e

https://rderik.com/blog/setting-up-access-to-a-private-repository-in-argocd-with-ssm-parameter-store-and-external-secrets-operator/

Setup ArgoCD and Github so argocd can have access to private github repos.

## Generate ssh key-pair
```
ssh-keygen -t rsa -b 4096 -C "key for argocd to access private repo" -f id_rsa_argocd_repo
```

## Add deploy key on GitHub repo
On the repository settings, Deploy keys -> Add deploy key -> add the generated public key
