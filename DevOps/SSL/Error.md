# Error

## Unable to get Local Issuer Certificate
The root certificates on the system are not working correctly, misconfigured, such as using a root ca cert that is not used to create the cert.

## IT department installed a firewall which intercepts SSL connections.
https://serverfault.com/questions/1100480/wsl-docker-curl-60-unable-to-get-local-issuer-certificate

## [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)
https://stackoverflow.com/questions/62952004/local-issuer-certificate-error-uniquely-in-docker-with-python

Solution: `export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`

Another case:\
https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f

The `consolidate.pem` should include all level crt files (root, intermediate, and local) in the chain
```
response = requests.post(url, files=files, headers=headers, verify='consolidate.pem')
```

## [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)

Cause: Could not find the root/intermediate ca crt files in the server

- Possible solution: `export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`
- Possible solution, if we have both root and intermediate ca files, both ca crt files should be installed in the trust store
  ```
  sudo cp root-ca.crt intermediate-ca.crt /usr/local/share/ca-certificates/extra/
  sudo update-ca-certificates
  ```
  If not will get the error: `certificate verify failed: self signed certificate in certificate chain`
- Right solution:
  - must put the server crt and the intermediate crt into one file
  - server crt first then intermediate crt: `cat server.crt intermediate-ca.crt > tls.crt`

## verify error:num=21:unable to verify the first certificate
https://pavolkutaj.medium.com/unable-to-verify-the-first-certificate-with-openssl-47eecb652a9b

This error means that the certificate chain is broken for OpenSSL — but does not have to be for browsers.
- The crt is not added to /etc/ssl/certs/ca-certificates.crt
- The pem converted from crt does not exist in /etc/ssl/certs
