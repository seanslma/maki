# service

if a service depends on another service, it might fail to start as the other service is not started yet. Perhaps need to consider using auto (DELAYED START) or using C# to start it if it stopped.

## service
Right click the 'service.cs' file and add installer.

```dos install_service.bat
@echo off

set exe="C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe"
set svi="C:\DemoService\MyService.exe"

rem install
%exe% %svi%

rem uninstall
rem %exe% /u %svi%

echo all done!
@pause
```

## event log
```c#
//set log
log = new System.Diagnostics.EventLog();
log.Source = "MyService";
log.Log = "MyLog";

//source needs to be created if it doesn't exist
((ISupportInitialize)log).BeginInit();
if (!EventLog.SourceExists(log.Source)) {
    EventLog.CreateEventSource(log.Source, log.Log);
}
((ISupportInitialize)log).EndInit();

//then use it
log.WriteEntry("My Eventlog Info message.", EventLogEntryType.Information);
log.WriteEntry("My Eventlog Err message.", EventLogEntryType.Error);
```

## control service

```csharp
using System.ServiceProcess;

var svc = new ServiceController(svcName);
var timeout = TimeSpan.FromMilliseconds(timeoutMilliseconds);
svc.Start();
svc.WaitForStatus(ServiceControllerStatus.Running, timeout);
svc.Refresh();

if (svc.Status==ServiceControllerStatus.Running) svc.Stop();
if (svc.Status==ServiceControllerStatus.Stopped) svc.Start();
```
