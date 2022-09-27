# Azure Libraries

Configure logging in the Azure libraries for Python

https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-logging

## Set logging levels
```
import logging

#for a specific library
logger = logging.getLogger('azure.identity.aio')
logger.setLevel(logging.ERROR)

#for all azure-storage-* libraries
logger = logging.getLogger('azure.storage')
logger.setLevel(logging.INFO)

#for all azure-* libraries
logger = logging.getLogger('azure')
logger.setLevel(logging.ERROR)
```
Note that the azure logger is used by some libraries instead of a specific logger. For example, the azure-storage-blob library uses the azure logger.
