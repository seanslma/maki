# Docker

## .NET SDK
The .NET SDK (Software Development Kit) is primarily used for building, developing, and running .NET applications.

To install dotnet-sdk: 
```dockerfile
RUN apt-get update \
    && apt-get install --yes dotnet-sdk-8.0
ENV dotnet_sdk="true"
```
