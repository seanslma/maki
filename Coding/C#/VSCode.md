# VS Code

## install package
```
dotnet add package Microsoft.Extensions.Configuration.Json --version 6.0.0
dotnet add package Microsoft.Extensions.Configuration.Binder --version 6.0.0
```

## vs build tools
it's free for comercial use: \
https://social.msdn.microsoft.com/Forums/en-US/0daefd5d-8d5a-499c-bd16-c3e7aba68c4d/is-msbuild-free-for-commercial-use?forum=msbuild

https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16

msbuild app.csproj -t:HelloWorld -p:Configuration=Release \
msbuild app.csproj -p:Configuration=Release
