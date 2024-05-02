# NuGet

https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-powershell

```
Tools > NuGet Package Manager > Package Manager Console
```

## solution package source
```
Solution/.nuget/NuGet.Config
```

## project package config
The `packages.config` file in a C# project is used to manage NuGet package dependencies in older project formats. 
```
Project/packages.config
```

A newer approach called `PackageReference` typically uses `.csproj` files to manage dependencies directly.

Migrate to the new approach:
https://learn.microsoft.com/en-us/nuget/consume-packages/migrate-packages-config-to-package-reference

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
```powershell
Update-Package <PackageName> -Version <newVersion> -ProjectName <ProjectName>
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

##  but the package does not contain any assembly references or content files that are compatible with that framework
```
Update-Package : Could not install package '<package-name>'.
You are trying to install this package into a project that targets '.NETFramework,Version=v4.6.1',
but the package does not contain any assembly references or content files that are compatible with that framework.
For more information, contact the package author.
```
Solution:
https://stackoverflow.com/questions/34991703/nuget-package-installation-failure
- goto `Tools->Options->Nuget->General` and clear the cache
