# Build

## build a c# app
`dotnet publish` is a .NET CLI command used for publishing a .NET application. 
- `publish` is the command used for publishing a .NET application.
  It compiles the application and its dependencies, and it prepares it for deployment.
- The `Release configuration` typically includes optimizations and is suitable for deployment in a production environment.
  Other common configurations include Debug for development and debugging.
```sh
set -eoux pipefail
unset VERSION

dotnet publish -c Release ./src/Dev.Sales.csproj

mkdir -p "${PREFIX}/lib/dotnet/shared/dev"
cp -r "${SRC_DIR}/src/bin/Release/net8.0/publish/" "${PREFIX}/lib/dotnet/shared/dev/dev-sales/"
```
