# Service Principal
A service principal (SP) in Azure Active Directory (AD) is a form of security identity. 

By default, service principals have a lifespan of one year before the password expires. 

Admins assign an Azure SP to an object, such as an automated tool, application or VM. Then, they use role-based access controls to manage that object's access to Azure resources, rather than use security credentials within scripts.

## create 
```
az ad sp create-for-rbac --name <service-principal-name> #default Contributor role
az ad sp create-for-rbac --name <service-principal-name> --role reader #Reader role

az login --service-principal --username <app-id> --password <password> --tenant <tenant-id>
az account show #get Azure Subscription ID and name
```
