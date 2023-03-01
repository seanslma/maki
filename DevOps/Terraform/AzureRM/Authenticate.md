# Authenticate

https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_cli

## authentication methods
When run locally use Azure CLI;
when run on CI server, use the others
- using Azure CLI (locally)
- using Managed Service Identity
- using a Service Principal and a Client Certificate
- using a Service Principal and a Client Secret
- using a Service Principal and Open ID Connect

```
az login --service-principal --username <client_id> --password <client_secret> --tenant <tenant_id>
```
