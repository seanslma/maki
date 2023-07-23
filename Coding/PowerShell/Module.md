# SSnapins and modules

List installed PSSnapins: `Get-PSSnapin –Registered`

List all modules: `Get-Module -ListAvailable`

Show env variable value: `$env:psmodulepath`

## check modules on a remote machine
```ps1
$session = New-PSSession -ComputerName Win8 #create a remote session
Get-Module -PSSession $session -ListAvailable
```

## entension
```ps1
Get-Module #display a list of all loaded modules
Remove-Module #unload a module
Import-Module storage #load entension
Get-Command -Module storage #show entension commands
ActiveDirectory\Get-ADUser #use extension to avoid conflict
Import-Module MyModule –Prefix DJR #add a prefix to all command to avoid conflict
$PSModuleAutoLoadingPreference #manage module auto loading
```
