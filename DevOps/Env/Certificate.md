# CVertificate

https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f

https://github.com/Azure/azure-cli/issues/5099

## self signed certificate err
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1091)

**soluation**:
  * set env var: will probably just break things
  ```
  set REQUESTS_CA_BUNDLE="path-to-my.crt"
  echo %REQUESTS_CA_BUNDLE%
  ```
  * pass crt to verify
  ```
  import requests
  url = 'https://test.web.com'
  r = requests.get(url, verify='path-to-my.crt')
  ```
  * best solution: python-certifi-win32 monkey-patches certifi (used by requests and most Python HTTP libs) so that it uses the Windows Certificate Store (where your local Certificate is located)
  ```
  install local certificate
  install python-certifi-win32
  ```
