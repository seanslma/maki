# Error

## Trouble shooting
https://learn.microsoft.com/en-us/powershell/azure/troubleshooting?view=azps-8.3.0


## Error: SharedTokenCacheCredential authentication unavailable
Run the command first:
```
Connect-AzAccount -Tenant <tenant-id>
```

## Error: command was found in the module 'Az.Accounts', but the module could not be loaded
have both the Az and AzureRM PowerShell modules installed on the same Windows-based system.

AzureRM PowerShell modules will be retired on 29 February 2024. Delete AzureRM:
```
Uninstall-AzureRm
```

module `Az.Compute` same error:

The 'Get-AzComputeResourceSku' command was found in the module 'Az.Compute', but the module could not be loaded. For more information, run 'Import-Module Az.Compute'.
