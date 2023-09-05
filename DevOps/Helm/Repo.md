# Chart repo

https://helm.sh/docs/topics/chart_repository/

## private repo with self-signed cert
https://github.com/helm/helm/issues/8868

not usable

## use github page as private helm repo
https://im5tu.io/article/2022/01/creating-a-private-helm-repository-using-github-pages-enterprise/

## use azure blob storage as private helm repo
Setting up secure helm chart repository on Azure Blob Storage

## disable ssl cert
```
helm repo add jh https://jupyterhub.github.io/charts --insecure-skip-tls-verify
```

## use `--ca-file`
```
helm repo add jh https://jupyterhub.github.io/charts --ca-file /path/to/ca-file
```
