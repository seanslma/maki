# NuGet

https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-powershell

```
Tools > NuGet Package Manager > Package Manager Console
```

## find all versions of a package
```powershell
Find-Package <PackageName> -AllVersions -ExactMatch
Find-Package <PackageName> -AllVersions -ExactMatch | Format-Table -Property Id,Versions,Description
```

## install a specific version of a package
```powershell
Install-Package <PackageName> -Version 4.4.1            # install to default project
Install-Package <PackageName> -ProjectName UtilitiesLib # install to a specific project
```

## update a package in all projects
```poershell
Get-Project -All | Update-Package <PackageName> -Version newVersion
```

## nuget cli
https://learn.microsoft.com/en-us/nuget/reference/nuget-exe-cli-reference?tabs=windows

### add a package source
```sh
nuget help
nuget source add -name "name" -source http://nuget.example.com/nuget/
nuget source # list all package sources
```

### list versions of a package
```sh
nuget list <package-id> -verbosity detailed                    # latest version: normal, quiet, detailed
nuget list <package-id> -source <source> -verbose -allversions # all versions
```
