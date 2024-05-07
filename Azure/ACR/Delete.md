# Delete

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-delete

## delete repo
```sh
az acr repository delete --name <acr-name> --repository <repo-name>
```

## delete by tag
```sh
az acr repository delete -n <acr-name> -t <repo-name>:<tag>
az acr repository delete --name <acr-name> --image <repo-name>:<tag>
```
