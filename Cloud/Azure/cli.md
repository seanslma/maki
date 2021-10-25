#Azure CLI

# resource group
```
az group create --name rg01 --location australiaeast
```

# List all regions
```
az account list-locations --output table #list all locations
az vm list-sizes --location "westus" #list available vm sizes in a specific location
```

# storage account
```
#create
az storage account create \
  --name <account-name> \
  --resource-group rg01 \
  --location australiaeast \
  --sku Standard_RAGRS \
  --kind StorageV2
  
  #delete
  az storage account delete --name <storage-account> --resource-group <resource-group>
```

# Connect to VM
```
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -Launch #connect to VM using PowerShell
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -LocalPath "C:\Path\to\folder" #save RDP file for future use
```
