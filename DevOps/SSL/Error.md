# Error

## Unable to get Local Issuer Certificate
The root certificates on the system are not working correctly, misconfigured, such as using a root ca cert that is not used to create the cert.

### IT department installed a firewall which intercepts SSL connections.
https://serverfault.com/questions/1100480/wsl-docker-curl-60-unable-to-get-local-issuer-certificate

### [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)
https://stackoverflow.com/questions/62952004/local-issuer-certificate-error-uniquely-in-docker-with-python

Solution: `export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`

### [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)
Solution: `export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`
