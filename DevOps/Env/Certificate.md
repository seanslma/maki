# Certificate

https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f

https://github.com/Azure/azure-cli/issues/5099

## certificate packages
- `python-certifi-win32` uses Windows certificate store to check the validity of certificates.
- newer versions of python use `certifi` package.

Show certificate path
```
import certifi
certifi.where()
```
Get self signed certificate from a server
```
openssl s_client -showcerts -connect server.com:443 </dev/null 2>/dev/null | openssl x509 -outform PEM >ca.pem
```

## self signed certificate err
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1091)

**soluation**:
  * set env var: will probably break things
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
  install certifi
  install python-certifi-win32
  ```
  
## Unable to get local issuer certificate
https://confluence.atlassian.com/bitbucketserverkb/ssl-certificate-problem-unable-to-get-local-issuer-certificate-816521128.html
 
popup window after run???
```
git config --global http.sslbackend schannel
```
