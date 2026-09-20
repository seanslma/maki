# NuGet

## install package from nuget console
```sh
Install-Package Apache.Arrow
Install-Package Apache.Arrow.Parquet
```

## dotnet build: error NU1301
```
Unable to load the service index for source
https://pkgs.dev.azure.com/<Organization>/_packaging/<Organization>/nuget/v3/index.json.
Response status code does not indicate success: 401 (Unauthorized).
```

Azure DevOps Artifacts authentication issues:
- https://github.com/NuGet/Home/wiki/Azure-DevOps-Artifacts-authentication-issues

**Solution**: Install the Azure Artifacts NuGet Credential Provider
- https://github.com/microsoft/artifacts-credprovider
- run the command from a folder outside of your project: `dotnet tool install --global  Microsoft.Artifacts.CredentialProvider.NuGet.Tool`
- run `dotnet restore --interactive`
- use a web browser to open the page https://login.microsoft.com/device and enter the code `***` to authenticate
