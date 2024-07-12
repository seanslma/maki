# workload identity

## migrate from pod-identity
- https://learn.microsoft.com/en-us/azure/aks/workload-identity-migrate-from-pod-identity
- https://blog.identitydigest.com/migrate-podid/
- https://www.codit.eu/blog/migrating-to-aad-workload-identity-on-azure-kubernetes-service-aks/?country_sel=be
- https://blog.novacare.no/moving-from-aad-pod-identity-to-workload-identity-in-aks/

## enable the OIDC Issuer in aks
https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer

create aks with `oidc-issuer`
```sh
az aks create -n myAKSCluster -g myResourceGroup \
    --node-count 1 \
    --enable-oidc-issuer \
    --generate-ssh-keys
```

enable `oidc-issuer` in existing aks
```sh
az aks update -n myAKSCluster -g myResourceGroup --enable-oidc-issuer
```

show oidc-issuer url
```sh
az aks show -n myAKScluster -g myResourceGroup --query "oidcIssuerProfile.issuerUrl" -o tsv
```

Rotate the OIDC key
```sh
az aks oidc-issuer rotate-signing-keys -n myAKSCluster -g myResourceGroup
```
