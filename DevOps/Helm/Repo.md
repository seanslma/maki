# Chart repo

https://helm.sh/docs/topics/chart_repository/

## use github page as private helm repo
https://im5tu.io/article/2022/01/creating-a-private-helm-repository-using-github-pages-enterprise/

## use azure blob storage as private helm repo
Setting up secure helm chart repository on Azure Blob Storage: 
https://cwienczek.com/2017/10/setting-up-secure-helm-chart-repository-on-azure-blob-storage/

## use azure container registry as private helm repo
https://learn.microsoft.com/en-us/azure/container-registry/container-registry-helm-repos
```sh
az acr login --name $ACR_NAME
helm push ingress-nginx-3.20.1.tgz oci://$ACR_NAME.azurecr.io/helm
az acr repository list --name $ACR_NAME
```
Helm Chart.yaml
```yaml
dependencies:
  - name: ingress-nginx
    version: 3.20.1
    repository: oci://$ACR_NAME.azurecr.io/helm
```
Get error using helm 3.8.0 due to bug: https://github.com/helm/helm/issues/10624
```
rpc error: code = Unknown desc = Manifest generation error (cached): 
`helm dependency build` failed exit status 1: Error: could not retrieve list of tags for repository oci://$ACR_NAME.azurecr.io/helm: 
GET "https://$ACR_NAME.azurecr.io/v2/helm/ingress-nginx/tags/list": 
GET "https://$ACR_NAME.azurecr.io/oauth2/token?scope=repository%3Ahelm%2Fingress-nginx%3Ametadata_read%2Cpull&service=$ACR_NAME.azurecr.io": 
unexpected status code 401: unauthorized: authentication required, visit https://aka.ms/acr/authorization for more information.
```
Solution: update to the latest helm version?

## private repo with self-signed cert
not usable: https://github.com/helm/helm/issues/8868

## disable ssl cert
```
helm repo add jh https://jupyterhub.github.io/charts --insecure-skip-tls-verify
```

## use `--ca-file`
```
helm repo add jh https://jupyterhub.github.io/charts --ca-file /path/to/ca-file
```
