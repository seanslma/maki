# Service Principal

## create 
```
az ad sp create-for-rbac --name <service-principal-name> #default Contributor role
az ad sp create-for-rbac --name <service-principal-name> --role reader #Reader role
az account show #get Azure Subscription ID and name
```
