# Setting

## disable prophet log
```
import logging
logging.getLogger('prophet').setLevel(logging.ERROR)
```

## diable cmdstanpy log
```
cmdstanpy_logger = logging.getLogger("cmdstanpy")
cmdstanpy_logger.disabled = True
```

## redirect cmdstanpy log
```
cmdstanpy_logger.disabled = False
cmdstanpy_logger.handlers = [] #remove all existing handlers
cmdstanpy_logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('cmdstanpy.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(
    logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        "%H:%M:%S",
    )
)
cmdstanpy_logger.addHandler(handler)
```
