# Basic

## run
```sh
./my.ps1
```
F7 will display the command history

Tab key to complete the PowerShell cmdlet, function, and parameter/variable names

Install ISE on server: `Add-WindowsFeature -Name PowerShell-ISE`

## help
`help` is a function and `man` is an alias to help. `help` and `man` run `Get-Help` under the hood, but they pipe its output to more.

`Update-Help` to download and install help files.

Help support wildcard: `help *service*`
```sh
help about*
help *send*mail* -Full #displays the full help
help *send*mail* -Examples #displays usage examples only
help *send*mail* -Detailed #displays details on each command parameter
help *send*mail* -ShowWindow #opens full help in a pop-up window
```
