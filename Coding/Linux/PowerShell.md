# PowerShell

## Show Env
```
Get-ChildItem Env:
```

## Profile location
Shows all profile file locations, whether or not the individual profile files exist.
```
$profile | select *  #short for: $PROFILE | Select-Object -Property *

AllUsersAllHosts       : /opt/microsoft/powershell/7/profile.ps1
AllUsersCurrentHost    : /opt/microsoft/powershell/7/Microsoft.PowerShell_profile.ps1
CurrentUserAllHosts    : /home/usr/.config/powershell/profile.ps1
CurrentUserCurrentHost : /home/usr/.config/powershell/Microsoft.PowerShell_profile.ps1
Length                 : 61
```

## Creating a PowerShell profile
***caveat***: the `PATH` must be all upper case.
```
pwsh
code $profile
#add sqlcmd/bcp path and restart terminal
$env:PATH += ":/opt/mssql-tools/bin"

#for bash
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile #login sessions
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc       #interactive sessions

#check
sqlcmd -?
```