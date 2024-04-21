# Azure CLI

https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest

## install
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt

ubuntu
```sh
# remove old version 2.0.81 package
sudo apt remove azure-cli -y && sudo apt autoremove -y
# install the latest version
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## upgrade
```sh
az version
az upgrade -y
az extension update --name aks-preview
```

if have legacy kubectl must be migrate to the new repo first:
https://kubernetes.io/blog/2023/08/15/pkgs-k8s-io-introduction/

## new line
- bash: use backslash \
- pwsh: use a backtick `
- batch: use accent circonflexe ^

## List all subscriptions
```sh
az account list --output table
az account set --subscription <subscription-id> #set default subscription
```

## List all regions
```sh
az account list-locations --output table #list all locations
az vm list-sizes --location "westus"     #list available vm sizes in a specific location
```

## resource group
```sh
az group list
az group list -o table
az group create --name rg01 --location australiaeast
az group delete --name rg01
```

## service principal
```sh
$sp = az ad sp create-for-rbac --name <sp-name> | ConvertFrom-Json
az ad sp create-for-rbac --name <sp-name> --role Contributor --scopes /subscriptions/<subscription-id>
```

## storage account
```sh
#create
az storage account create --name <storage-account-name> `
--resource-group rg01 --location australiaeast --sku Standard_RAGRS --kind StorageV2

#delete
az storage account delete --name <storage-account-name> --resource-group <resource-group>
```

## key vault
```sh
az keyvault create --location $region --name <kv-name> `
--resource-group <resource-group> --enabled-for-template-deployment true

az keyvault secret set --name <secret-name> --value $sp.password --vault-name <vault-name>
az keyvault secret set --name <secret-name> --value "A string value" --vault-name <vault-name>

#allow pipeline to access the keyvault
az keyvault set-policy --name <name> --spn $spIdUri --secret-permissions get list
```

## Connect to VM
```sh
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -Launch #connect to VM using PowerShell
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -LocalPath "C:\Path\to\folder" #save RDP file for future use
```
