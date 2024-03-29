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

## run terraform using service principle
```
export ARM_SUBSCRIPTION_ID="<subscription_id>"
export ARM_TENANT_ID="<tenant_id>"
export ARM_CLIENT_ID="<client_id>"
export ARM_CLIENT_SECRET="<client_secret>"
```

## error: logged in using Azure CLI cannot use service principle
solution:
- Make sure logged in using the right directory
- Must login use the terminal not the vs code terminal as vs code terminal has restricted permission

## Error while retrieving OAuth token: Code Expired
```
Error: 
Get "https://<aks-name>.hcp.<region>.azmk8s.io:443/api/v1/namespaces/<namespace>": 
  acquiring a token for authorization header: failed acquiring new token: waiting for device code authentication to complete: 
  autorest/adal/devicetoken: Error while retrieving OAuth token: Code Expired
```  
Reason: the aks config file not in the right path so could not connetc to the aks.
