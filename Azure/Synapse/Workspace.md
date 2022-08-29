# Synapse Workspace

## Create Azure Synapse Analytics workspace
Install
```
Install-Module Az.Resources  
Install-Module Az.Sql 

Connect-AzAccount #login
```

Then run pwsh to register resource providers:
- Microsoft.Synapse
- Microsoft.Sql
- Microsoft.Storage
- Microsoft.Compute

And create:
- Resource group
- Synapse Analytics workspace
    - a Storage account for your data lake, 
    - an Apache Spark pool, 
    - a Data Explorer pool, and 
    - a Dedicated SQL pool.
