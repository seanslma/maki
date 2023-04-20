# Install

## uninstall AzureRM
AzureRM and AZ cannot be co-exist:
`We do not support having both the AzureRM and Az PowerShell modules installed in Windows PowerShell 5.1 at the same time`
```
Uninstall-AzureRm #prefered method?
Uninstall-Module -Name AzureRM -AllVersions
```

## install AZ
```
Install-Module -Name Az -Repository PSGallery -Force
Update-Module -Name Az -Force
```
