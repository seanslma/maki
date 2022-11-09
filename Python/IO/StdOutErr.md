# StdOutErr

## dup, dup2, tmpfile and stdout in python
https://stackoverflow.com/questions/8817993/dup-dup2-tmpfile-and-stdout-in-python/8825434#8825434

python's sys.stdout is a wrapper of the actual stdout handler so redirect sys.stdout will not affect the stdout messaged from other languages such as C and C++.

We need to duplicate the acutal stdout (1) using os.dup and os.dup2 to redirect the messages.
