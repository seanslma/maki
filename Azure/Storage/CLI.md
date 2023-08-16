# CLI

## storage account
```sh
# list storage accounts
az storage account list -o table
# show storage account properties
az storage account show --name <account-name> --resource-group <resource-group>
# get storage account id
az storage account show --name <account-name> --resource-group <resource-group> --query id
# update storage account property
az storage account update --name <account-name> --resource-group <resource-group> --allow-cross-tenant-replication false
```

## storage container
```sh
# list storage containers
az storage container list --account-name <account-name> -o table --auth-mode login
# show storage container properties
az storage container show --name <container-name> --account-name <account-name> --auth-mode login
```
