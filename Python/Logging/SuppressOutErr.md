# Suppress stdout and stderr

## works for stdout and stderr from c as well
https://github.com/facebook/prophet/issues/223
```
class SUPPRESS_STDOUT_STDERR(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).
    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = [os.dup(1), os.dup(2)]

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)
        # https://stackoverflow.com/questions/66784941/dup2-and-pipe-shenanigans-with-python-and-windows
        if sys.platform == 'win32':
            sys.stdout.write = lambda z: os.write(
                sys.stdout.fileno(),
                z.encode() if hasattr(z, 'encode') else z
            )        

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        # Close the null files
        for fd in self.null_fds + self.save_fds:
            os.close(fd)
```

https://medium.com/swlh/python-recipes-suppress-stdout-and-stderr-messages-9141ef4b1373

## redirect stdout and stderr to file
https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/

https://dzone.com/articles/redirecting-all-kinds-stdout

https://devpress.csdn.net/python/62fd8a92c677032930803e01.html
