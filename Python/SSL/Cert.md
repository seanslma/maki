# Cert

## check https call OK
```py
import requests
requests.post('https://my.example.com/EWS/Exchange.asmx')

import requests
requests.get('https://my.example.com/', verify=False)
requests.get('https://my.example.com/', verify='/etc/ssl/certs/ca-certificates.crt')
```

## show cert path
```py
#option 1
from requests.utils import DEFAULT_CA_BUNDLE_PATH
print(DEFAULT_CA_BUNDLE_PATH)

#option2
import certifi
certifi.where()
```
