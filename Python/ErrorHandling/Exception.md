# Exception

## except vs except Exception
```py
try:
    x = 1 / 0
except: # except Exception as exc:
    x = 0
```
We should never use a bare `except`! 

https://docs.python.org/3.1/howto/doanddont.html \
```
Python has the `except:` clause, which catches all exceptions. 
Since every error in Python raises an exception, using `except:`
can make many programming errors look like runtime problems, which hinders the debugging process.

Because except: catches all exceptions, including SystemExit, KeyboardInterrupt, and GeneratorExit
(which is not an error and should not normally be caught by user code), using a bare except: is almost never a good idea.
In situations where you need to catch all “normal” errors, such as in a framework that runs callbacks,
you can catch the base class for all normal exceptions, Exception.
```

We should use the most specific exception possible and if we do want to catch all exceptions
we should catch `Exception` which is the base class of all normal exceptions. 

We should also capture the exception with `as exc` as it is very useful to have if we are in the debugger inside the except block.

## exception hierarchy
https://docs.python.org/3.10/library/exceptions.html#exception-hierarchy

