# format

```cs
//format
string msg = $"Delayed time: {hrs:D2}:{mts:D2}:{sec:00.000}";

//StopWatch Elapsed to hh:mm:ss.fff
string time = $"elapsed time: {sw.Elapsed:hh\\:mm\\:ss\\.ffff}";

//Utc to AEST Brisbane time
var aestZone = TimeZoneInfo.FindSystemTimeZoneById("E. Australia Standard Time");
date = TimeZoneInfo.ConvertTimeFromUtc(utcTime, aestZone);

//integer left pad spaces
$"{i,15:D}"
//double left pad spaces
$"{v,15:N4}"
```
