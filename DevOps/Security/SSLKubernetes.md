# SSl Kubernetes

## show cert details
```
openssl x509 -noout -text -in tls.crt
```

## validate cert
Will show server certificate details
```
curl https://my.example.com -kv
```

## kube ingress tls
Not show the details about creating the cert

https://devopscube.com/configure-ingress-tls-kubernetes/

## create root crt with details
https://medium.com/@tbusser/creating-a-browser-trusted-self-signed-ssl-certificate-2709ce43fd15

### Create root certificate
create a private key
```
openssl genrsa -des3 -passout pass:<pwd> -out root.key 2048
```

generate root certificate
```
openssl req -x509 -new -nodes -key root.key -sha256 -days 1024  -out root.pem
```
Input info required:
- Country Name (2 letter code) [AU]:NL
- State or Province Name (full name) [Some-State]:.
- Locality Name (eg, city) []:<city>
- Organization Name (eg, company) [Internet Widgits Pty Ltd]:<O:company name>
- Organizational Unit Name (eg, section) []:<OU:company unit name>
- Common Name (e.g. server FQDN or YOUR name) []:<>
- Email Address []:<my@email.com>

### Create the SSL certificate
`alt_names` can add one or more DNSs.
  
v3.ext
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

create private key for SSL certificate and certificate signing request
```
openssl req -new -nodes -out server.csr -newkey rsa:2048 -keyout server.key
```
Also requires some info input.
  
issue the certificate with the previously generated root certificate
```
openssl x509 -req -in server.csr -CA root.pem -CAkey root.key -CAcreateserial -out server.crt -days 500 -sha256 -extfile v3.ext  
```

### combine `server.key` and `server.crt` into single file
```
openssl pkcs12 -inkey server.key -in server.crt -export -out server.pfx  
```  
  
## kube certi 3 methods
https://kubernetes.io/docs/tasks/administer-cluster/certificates/

## 4 methods
https://phoenixnap.com/kb/kubernetes-ssl-certificates

##
https://kuberty.io/blog/how-to-generate-a-self-signed-certificate-for-kubernetes-2/
