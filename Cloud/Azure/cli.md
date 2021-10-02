#Azure CLI

# List all regions
```cli
az account list-locations --output table #list all locations
az vm list-sizes --location "westus" #list available vm sizes in a specific location
```

# Connect to VM
```
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -Launch #connect to VM using PowerShell
Get-AzRemoteDesktopFile -ResourceGroupName "RgName" -Name "VmName" -LocalPath "C:\Path\to\folder" #save RDP file for future use
```
