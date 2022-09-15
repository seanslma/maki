# Azure CLI

https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest

## List all subscriptions
```
az account list --output table
az account set --subscription <subscription-id> #set default subscription
```

## List all regions
```
az account list-locations --output table #list all locations
az vm list-sizes --location "westus" #list available vm sizes in a specific location
```

## resource group
```
az group create --name rg01 --location australiaeast
az group delete --name rg01
```

## service principal
```
$sp = az ad sp create-for-rbac --name <sp-name> | ConvertFrom-Json
az ad sp create-for-rbac --name <sp-name> --role Contributor --scopes /subscriptions/<subscription-id>
```

## storage account
```
#create
az storage account create --name <storage-account-name> `
--resource-group rg01 --location australiaeast --sku Standard_RAGRS --kind StorageV2
  
#delete
az storage account delete --name <storage-account-name> --resource-group <resource-group>
```

## key vault
```
az keyvault create --location $region --name <kv-name> `
--resource-group <resource-group> --enabled-for-template-deployment true
  
az keyvault secret set --name <secret-name> --value $sp.password --vault-name <vault-name>
az keyvault secret set --name <secret-name> --value "A string value" --vault-name <vault-name>

#allow pipeline to access the keyvault
az keyvault set-policy --name <name> --spn $spIdUri --secret-permissions get list
```

## Connect to VM
```
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -Launch #connect to VM using PowerShell
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -LocalPath "C:\Path\to\folder" #save RDP file for future use
```
