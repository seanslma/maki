# workload identity

## docs
https://azure.github.io/azure-workload-identity/docs/

- user managed identity -> federated credential (new) -> service account (azure_identity)
- service account (azure_identity, azure_identity_binding) -> pod

## mutating admission webhook
https://azure.github.io/azure-workload-identity/docs/installation/mutating-admission-webhook.html

## Migrate from pod-identity
- https://learn.microsoft.com/en-us/azure/aks/workload-identity-migrate-from-pod-identity
- https://blog.identitydigest.com/migrate-podid/
- https://www.codit.eu/blog/migrating-to-aad-workload-identity-on-azure-kubernetes-service-aks/?country_sel=be
- https://blog.novacare.no/moving-from-aad-pod-identity-to-workload-identity-in-aks/

## Enable the OIDC Issuer in AKS
https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer
```sh
# create aks with oidc-issuer enabled
az aks create -n my_aks -g my_rg --node-count 1 --generate-ssh-keys --enable-oidc-issuer

# enable oidc-issuer in existing aks
az aks update -n my_aks -g my_rg --enable-oidc-issuer
# show oidc-issuer url
az aks show -n my_aks -g my_rg --query "oidcIssuerProfile.issuerUrl" -o tsv
# rotate oidc key
az aks oidc-issuer rotate-signing-keys -n my_aks -g my_rg
```

## Install azure workload identity webhook controller
https://www.blakyaks.com/resources/using-azure-workload-identity-on-aks

- This can be done with `--enable-workload-identity` when creating aks. 
- But the helm chart allows customization like namespace, tolerations, etc.
```sh
# install workload-identity-webhook
helm repo add azure-workload-identity https://azure.github.io/azure-workload-identity/charts
helm repo update
helm install workload-identity-webhook azure-workload-identity/workload-identity-webhook \
  --namepace workload-identity-system \
  --create-namespace \
  --set azureTenantID="${AZURE_TENANT_ID}"

# check webhook controller manager
kubectl get po -n workload-identity-system
```

## Replace `AzureIdentity` and `AzureIdentityBinding` by pod `ServiceAccount`
https://blog.novacare.no/moving-from-aad-pod-identity-to-workload-identity-in-aks
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-workload-identity
  namespace: dev
  annotations:
    azure.workload.identity/client-id: 00000000-0000-0000-0000-000000000000  
```
In deployment replace
```yaml
spec:
  selector:
    matchLabels:
      component: web
      aadpodidbinding: my-service
```
by
```yaml
spec:
  selector:
    matchLabels:
      component: web
      azure.workload.identity/use: 'true'
  template:
    metadata:
      labels:
        component: web
        azure.workload.identity/use: 'true'
    spec:
      serviceAccountName: my-service-workload-identity
      containers:
      ...
```
