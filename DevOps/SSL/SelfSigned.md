# Browser SSL self-signed

renew ssl\
https://www.golinuxcloud.com/renew-self-signed-certificate-openssl/

create browser SSL self-signed certificate with details:\
https://medium.com/@tbusser/creating-a-browser-trusted-self-signed-ssl-certificate-2709ce43fd15

## why need tls.crt in the client machine
The package you received contains the certificate from that website. 
The tls.crt in the client machine is used to verify that the package is not modified in the middle.

For a self-signed certificate, if we do not have the local tls.crt we will get the error `self signed certificate in certificate chain`.
To avoid the issue, we need to copy the tls.crt to `/etc/ssl/certs` or `/usr/local/share/ca-certificates/extra` and run `update-ca-certificates`.

## Create root certificate
### create a private key
```
openssl genrsa -des3 -passout pass:<pwd> -out root.key 2048
```

### generate root certificate
```
openssl req -x509 -new -nodes -key root.key -sha256 -days 1000 -out root.pem
```
Input info required:
- Country Name (2 letter code) [AU]:NL
- State or Province Name (full name) [Some-State]:.
- Locality Name (eg, city) []:<city>
- Organization Name (eg, company) [Internet Widgits Pty Ltd]:<company name>
- Organizational Unit Name (eg, section) []:<company unit name>
- Common Name (e.g. server FQDN or YOUR name) []:<my.example.com>
- Email Address []:<>

## Create SSL certificate
### v3.ext
```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = example.com
DNS.2 = example2.com.dev
DNS.3 = *.example.com
```
`alt_names` can add one or more DNSs.  

### create private key for SSL certificate and certificate signing request
```
openssl req -new -nodes -out server.csr -newkey rsa:2048 -keyout server.key
```
Also requires some info input.
  
### issue the certificate with the previously generated root certificate
```
openssl x509 -req -in server.csr -CA root.pem -CAkey root.key -CAcreateserial -out server.crt -days 500 -sha256 -extfile v3.ext  
```

## combine `server.key` and `server.crt` into single file
```
openssl pkcs12 -inkey server.key -in server.crt -export -out server.pfx  
```  
