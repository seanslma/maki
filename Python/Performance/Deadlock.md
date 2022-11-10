# deadlock

https://pythonspeed.com/articles/python-multiprocessing/

In Python 3 the multiprocessing library added new ways of starting subprocesses. One of these does a fork() followed by an execve() of a completely new Python process. 

## global
```
from multiprocessing import set_start_method
set_start_method("spawn")
```

## local
```
from multiprocessing import get_context
def your_func():
    with get_context("spawn").Pool() as pool:
        # ... everything else is unchanged
```

## Start Method
A start method is the technique used to start child processes in Python.
- spawn: start a new Python process.
- fork: copy a Python process from an existing process.
- forkserver: new process from which future forked processes will be copied.

## default Start Methods
- Windows (win32): spawn
- macOS (darwin): spawn
- Linux (unix): fork
