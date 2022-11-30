# StdOutErr

## print message not shown
can be caused by buffer
```
print('ok', flush=True)
```

## dup, dup2, tmpfile and stdout in python
https://stackoverflow.com/questions/8817993/dup-dup2-tmpfile-and-stdout-in-python/8825434#8825434

python's sys.stdout is a wrapper of the actual stdout handler so redirect sys.stdout will not affect the stdout messaged from other languages such as C and C++.

We need to duplicate the acutal stdout (1) using os.dup and os.dup2 to redirect the messages.

## windows: OSError: incorrect function
https://stackoverflow.com/questions/66784941/dup2-and-pipe-shenanigans-with-python-and-windows

sys.stdout is an object of type TextIOWrapper, whose sys.stdout.write() method eventually calls either os.write() or the C equivalent, on the filedescriptor sys.stdout.fileno(), which is 1. 

- There are several types of filedescriptors: files, sockets, serial ports, terminals, pipes, etc... 
- The C library functions write(), close(), etc... work on mostly any type of filedescriptor, but some features only work when the filedescriptor is of a suitable type. 
- At creation time, the TextIOWrapper that is sys.stdout examines its filedescriptor (1) and determines that it's a terminal. 
- On Windows only, sys.stdout.write() ends up doing some operations that are only valid if the filedescriptor 1 is truly a terminal. 
- Once you os.dup2() so that 1 becomes an os.pipe() or file, and not a terminal, the Windows Python implementation crashes when it attempts to do terminal-specific operations on a pipe.

As a workaround, on Windows only, I'm doing 
```
if sys.platform == 'win32':
    sys.stdout.write = lambda z: os.write(
        sys.stdout.fileno(),
        z.encode() if hasattr(z, 'encode') else z
    )
```
