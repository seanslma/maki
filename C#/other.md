# other

## doc
https://docs.microsoft.com/en-us/dotnet/standard/events/observer-design-pattern

## check dll/exe .net version
``` powershell
$path = "C:\scripts\my.dll"
[Reflection.Assembly]::ReflectionOnlyLoadFrom($path).CustomAttributes |
Where-Object {$_.AttributeType.Name -eq "TargetFrameworkAttribute" } | 
Select-Object -ExpandProperty ConstructorArguments | 
Select-Object -ExpandProperty value
```

## data exchange with matlab
https://au.mathworks.com/help/matlab/ref/putfullmatrix.html

System.Net.Http.Formatting nuget package has been replaced by Microsoft.AspNet.WebApi.Client

