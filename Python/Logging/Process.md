# Process

## psutil
List process pid and name
```
import psutil
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print(f'pid: {proc.pid}, name: {proc.name()}')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
```
