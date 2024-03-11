# Rest API

https://learn.microsoft.com/en-us/cli/azure/use-azure-cli-rest-command?tabs=bash

## Using rest api to patch blockblobstorage property
In windows terminal, we escape the double quote by backslash
```
az rest --method get --url xxx

az rest --method patch
--url https://management.azure.com/subscriptions/subscription_id/resourceGroups/resource_group_id/providers/Microsoft.Storage/storageAccounts/block_blob_storage_name?api-version=2023-05-01
--body "{\"properties\": {\"accessTier\": null}}"
```

in linux
```
--body '{"properties": {"accessTier": null}}'
```
