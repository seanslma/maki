# Object

## show object members
```ps1
Get-Service | Get-Member #alias is gm
```
## sorting
```ps1
get-process | sort-object -Property vm -Descending #get-process | sort vm -desc
```
## selecting
### choosing properties
```ps1
Get-Process | Select-Object -Property Name,ID,VM,PM #get-porcess | select name, id, vm, pm
```
### choosing a subset objects
```ps1
Get-Process | sort VM -Descending | select -first 5 #select five processes using most virtual memory
Get-Process | sort PM -Descending | select -last 5  #select five processes using least amount of paged memory
Get-Process | sort PM -Descending | select -skip 3 -first 5 #skip first 3 first
measure-command {1..5000 | select -first 5 -wait} #will process all
```
### making custom properties
```ps1
#shorter version: get-process | select name, id, @{n="TotMem";e={$_.PM + $_.VM}}
Get-Process | Select –Property Name,ID,@{name="TotalMemory";expression={$_.PM + $_.VM}}
Get-Process | Select -Property Name,ID,@{name="TotalMemory(MB)";expression={($_.PM + $_.VM) / 1MB -as [int]}}
Get-Process | Select -Property Name,ID,@{name="VirtMem";expression={$psitem.vm}}, @{name="PhysMem";expression={$psitem.pm}}
```
### extracting and expanding properties
