# Cert

## requests certs
`Requests` maintainers bundled their own certs.
- Redhat `/etc/pki/ca-trust`
- Ubuntu `/etc/ssl/certs/`
- Windows `windows trust store`

## force using certs from system
```
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```
`/etc/ssl/certs/ca-certificates.crt` includes both:
- certificates provided by Ubuntu distribution and
- certificates added by user (/usr/local/share/ca-certificates/)

Note: If `verify` is set to a path to a directory, the directory must have been processed using the c_rehash utility supplied with OpenSSL.

## check https call OK
```sh
curl -vvvv https://my.example.com/EWS/Exchange.asmx
```

```py
import requests
requests.post('https://my.example.com/EWS/Exchange.asmx')

import requests
requests.get('https://my.example.com/', verify=False)
requests.get('https://my.example.com/', verify='/etc/ssl/certs/ca-certificates.crt')
```

## self-signed certificate in certificate chain
Python `requests.get` will throw the error (in windows):
```
SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1010)')))
```
Solution (or add to env vars):
```py
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'c:/cert-path/cert.crt'
# os.environ['SSL_CERT_FILE'] = 'c:/cert-path/cert.crt' # not required
requests.get('https://my.example.com/')
...
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
