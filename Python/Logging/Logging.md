# Logging

## log formatter
```
def get_log_formatter(message_prefix: str = None):
    log_format = ' | '.join([
        '%(asctime)s',
        '%(levelname)s',
        '%(name)s',
        '%(module)s',
        '%(funcName)s',
        '%(lineno)d',
        f{message_prefix}'%(message)s',
    ])
    return logging.Formatter(log_format)
```

## log to both stadout and file
```
import sys
import logging

log_formatter = get_log_formatter()

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
console_handler.setFormatter(log_formatter)
root_logger.addHandler(concole_handler)
package_logger.addHandler(console_handler)

#file handler
file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)
package_logger.addHandler(file_handler)
```

## Change logger formatter
```
logger = logging.getLogger()
log_formatter = get_log_formatter('[OK] | ')

#set new format to each logger
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
for handler in logger.handlers:
    handler.setFormatter(log_formatter)
```
