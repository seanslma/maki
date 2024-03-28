# API

## check aks api version
https://github.com/Azure/AKS/issues/3639
```sh
API_VERSION=2022-04-02-preview
az monitor activity-log list --offset 30d --max-events 10000 --namespace microsoft.containerservice --query "[?eventName.value == 'EndRequest' && contains(not_null(httpRequest.uri,''), '${API_VERSION}')]"
```
