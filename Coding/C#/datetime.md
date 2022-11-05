# DateTime

## datetime format
```c#
Console.WriteLine($"Current date time is: {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
```

## timzezone
```c#
var aestZone = TimeZoneInfo.FindSystemTimeZoneById("E. Australia Standard Time");
var dtnow = TimeZoneInfo.ConvertTimeFromUtc(DateTime.UtcNow, aestZone);
```
