# Logging
https://docs.python.org/3/library/logging.handlers.html

The `StreamHandler` class, located in the core logging package, sends logging output to streams such as sys.stdout, sys.stderr or any file-like object (or, more precisely, any object which supports write() and flush() methods).

The `FileHandler` class inherits the output functionality from StreamHandler.

## log formatter
```
def get_log_formatter(message_prefix: str = None) -> logging.Formatter:
    log_format = ' | '.join([
        '%(asctime)s',
        '%(levelname)s',
        '%(name)s',
        '%(module)s',
        '%(funcName)s',
        '%(lineno)d',
        f'{message_prefix}%(message)s',
    ])
    return logging.Formatter(log_format)
    
def set_log_message_prefix(message_prefix: str = None) -> None:
    """Set the log message prefix during run"""
    logger = logging.getLogger()
    log_formatter = get_log_formatter(message_prefix=message_prefix)

    #set new format to each logger
    #console_handler = logging.StreamHandler() #this handler is already in the handlers list
    #console_handler.setFormatter(log_formatter)    
    for handler in logger.handlers:
        handler.setFormatter(log_formatter)    
```

## log to both stadout and file
```
import sys
import logging

formatter = get_log_formatter()

#root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.ERROR)

#package logger
package_logger = logging.getLogger('package_log_name')
package_logger.setLevel(logging.INFO)
package_logger.propagate = False

#console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
root_logger.addHandler(concole_handler)
#if previous console handler not deleted, log will output multiple times
package_logger.addHandler(console_handler) 

#file handler
file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)
package_logger.addHandler(file_handler)
```
