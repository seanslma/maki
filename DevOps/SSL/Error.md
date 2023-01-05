# Error

## Unable to get Local Issuer Certificate
The root certificates on the system are not working correctly, misconfigured, such as using a root ca cert that is not used to create the cert.

### IT department installed a firewall which intercepts SSL connections.
https://serverfault.com/questions/1100480/wsl-docker-curl-60-unable-to-get-local-issuer-certificate

### [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)
https://stackoverflow.com/questions/62952004/local-issuer-certificate-error-uniquely-in-docker-with-python

Solution: `export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`

Another case:\
https://levelup.gitconnected.com/solve-the-dreadful-certificate-issues-in-python-requests-module-2020d922c72f

The `consolidate.pem` should include all level crt files (root, intermediate, and local) in the chain
```
response = requests.post(url, files=files, headers=headers, verify='consolidate.pem')
```

### [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)
Solution: `export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`

Solution case 2: If the ca has both root and intermediate cas, both ca crt files should be installed in the trust store
```
sudo cp root-ca.crt intermediate-ca.crt /usr/local/share/ca-certificates/extra/
sudo update-ca-certificates
```
