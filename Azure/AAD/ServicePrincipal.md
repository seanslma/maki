# Service Principal
A service principal (SP) in Azure Active Directory (AD) is a form of security identity:
- Create an App registration with a Service Principal
- Add app credential as a client secret (password string) or a certificate
- By default, service principals have a lifespan of one year before the password expires

Admins assign an Azure SP to an object, such as an automated tool, application or VM.
Then, they use role-based access controls to manage that object's access to Azure resources,
rather than use security credentials within scripts.

## issues, risks and management overhead
- App credentials has a limited lifetime and requires to be rolled from time to time
- Expired credentials can lead to downtime for the services utilizing the credential
- App credentials (especially client secrets ) sometimes are directly exposed as clear text to code

## create
```
az ad sp create-for-rbac \
  --name <service-principal-name> \
  --role reader #Reader role

az ad sp create-for-rbac \
  --name "<service-principal-name>" \
  --role "Contributor" \
  --scopes "/subscriptions/<subscription-id>"

az login --service-principal \
  --username <app-id> --password <password> \
  --tenant <tenant-id>

az account show #get Azure Subscription ID and name
```
