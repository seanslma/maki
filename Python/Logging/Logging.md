# Logging

## log to both stadout and file
```
import sys
import logging

log_formatter = logging.Formatter(' | '.join([
    '%(asctime)s',
    '%(levelname)s',
    '%(name)s',
    '%(module)s',
    '%(funcName)s',
    '%(lineno)d',
    '%(message)s',
]))

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
root_logger.addHandler(stdout_handler)
package_logger.addHandler(console_handler)

#file handler
file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)
package_logger.addHandler(file_handler)
```
