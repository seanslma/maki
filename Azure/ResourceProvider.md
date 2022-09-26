# Resource Provider

https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types

An Azure resource provider is a collection of REST operations that provide functionality for an Azure service.

## Register resource provider
- Some are registered by default
- Other are registered automatically when you take certain actions
- In some scenarios, a resource provider needs to be registered manually
```
az provider register --namespace Microsoft.KeyVault
```

## Show resource provider
Show all resource providers and status
```
az provider list \
    --query "[].{Provider:namespace, Status:registrationState}" \
    --out table
```

Show all registered resource providers
```
az provider list \
    --query "sort_by([?registrationState=='Registered'].{Provider:namespace, Status:registrationState}, &Provider)" \
    --out table
```

Show a perticular resource provider
```
az provider show --namespace Microsoft.KeyVault
```

Show resource provider type
```
az provider show --namespace Microsoft.KeyVault \
    --query "resourceTypes[*].resourceType" \
    --out table
```

Show resource provider available API versions
```
az provider show --namespace Microsoft.KeyVault \
    --query "resourceTypes[?resourceType=='batchAccounts'].apiVersions | [0]" \
    --out table
```

Show resource provider supported locations
```
az provider show --namespace Microsoft.KeyVault \
    --query "resourceTypes[?resourceType=='batchAccounts'].locations | [0]" \
    --out table
```
