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

## nuget cli
https://learn.microsoft.com/en-us/nuget/reference/nuget-exe-cli-reference?tabs=windows
```sh
nuget help
nuget list <package-id> -Verbosity detailed
```
