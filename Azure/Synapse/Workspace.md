# Synapse Workspace

## Create Azure Synapse Analytics workspace
Install
```
Install-Module Az.Resources  
Install-Module Az.Storage   #Get-AzStorageAccount, Set-AzStorageBlobContent
Install-Module Az.Sql
```
Install sqlcmd and bcp (bulk copy program):
```
Install-Module -Name SqlServer #does not help
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
sudo apt update && sudo apt install mssql-tools unixodbc-dev
```
Set the `sqlcmd` and `bcp` path - see `Linux/PowerShell/Creating a PowerShell profile`.
 
`Connect-AzAccount #login`

Then run pwsh to register resource providers:
- Microsoft.Synapse
- Microsoft.Sql
- Microsoft.Storage
- Microsoft.Compute

And create:
- Resource group
- Synapse Analytics workspace    
    - SQL pools 
    - Apache Spark pools
    - Data Explorer pools
    - Storage account for data lake
    
