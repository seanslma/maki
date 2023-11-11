# priority

^Priority Level ID ^Priority Level Name ^
|256 |Realtime |
|128 |High |
|32768 |Above normal |
|32 |Normal |
|16384 |Below normal |
|64 |Low |

## Change Priority of Running Process in Command Prompt
```bat
wmic process where name="mspaint.exe" CALL setpriority "Above normal"
```

## Start Application with a Set Priority in Command Prompt
```bat
start "" /AboveNormal /B "C:\Windows\System32\mspaint.exe" > out.txt
```

## set the IO priority of a process
It looks like the "real" way to set the IO priority of a process is using NtSetInformationProcess with the ProcessIoPriority information class. Unfortunately this API is undocumented, but you can see it in action by attaching a debugger to taskeng.exe and breaking in ExeTask::GetYourPrioritiesStraight.

I believe the PROCESS_INFORMATION_CLASS value for ProcessIoPriority is 33 (0x21), and the priority values are as follows:
- Very Low: 0
- Low: 1
- Normal: 2
- High: 3 or above?
