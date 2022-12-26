# SSL
https://www.keyfactor.com/resources/how-to-check-ssl-certificate/

## Types of SSL certificates
- Domain Validated Certificate (DV)
- Organization Validated Certificate (OV)
- Extended Validation Certificate (EV)

## Create self-signed SSL certificate
create a `my-site.crt` file based on input `my-site.csr`
```
openssl x509 -signkey my-site.key -in my-site.csr -req -days 365 -out my-site.crt
```

create a `cert.pem` based on pwd and pfx
```
SET pwd=mypwd
SET pfx_filepath=C:/tmp/cert.pfx
openssl req -x509 -sha256 -nodes -days 730 -newkey rsa:2048 -keyout private_key.key -out cert.crt -subj /CN=*.example.com
openssl pkcs12 -export -out %pfx_filepath% -inkey private_key.key -in cert.crt -password pass:%pwd%
openssl pkcs12 -in %pfx_filepath% -out cert.pem -nodes
```

## Renew SSL Certificate
- Generate a CSR (Certificate Signing Request)
- Select your SSL certificate and enter the required details like the validity period you need and other details and submit it to the CA. 
- You will get renewed certificate files which you can use on your server. 
- Renewing SSL certificates will require you to complete the same procedures you did for getting a new SSL certificate. These could be domain validation, organizational validation, and other verifications as needed for the level of certificate you are applying to the CA for.
