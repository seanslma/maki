# OpenSSL
https://medium.com/@superseb/get-your-certificate-chain-right-4b117a9c0fce

## version
```
openssl version -d
```

## check cert
```
openssl rsa -check -in server.key 
openssl x509 -noout -text -in server.crt
openssl req -noout -text -verify -in server.csr
```

## check key / cert match
```
openssl rsa -noout -modulus -in server.key | openssl md5
openssl x509 -noout -modulus -in server.crt | openssl md5
```

## verify certificate chain
`-untrusted` to provide intermediate certificate
```
openssl verify cert.pem
openssl verify -CAfile ca.pem cert.pem
openssl verify -CAfile RootCert.crt -untrusted Intermediate.crt UserCert.crt
```

## verify certificate
```
openssl s_client -connect <hostname>:<port>
openssl s_client -connect dev.example.com:443 -CApath /etc/ssl/certs
```

## with config file
```
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -days 365 -key ca.key -out ca.crt -subj "/CN=my.example.com"

openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -config csr.conf
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -extensions v3_ext -extfile csr.conf
```

## use passphrase
```
openssl genrsa -des3 -out ca.key 2048
openssl req -x509 -new -nodes -days 365 -key ca.key -sha256 -out ca.pem

openssl req -new -nodes -out server.csr -newkey rsa:2048 -keyout server.key
openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.crt -sha256 -extfile v3.ext
openssl pkcs12 -inkey server.key -in server.crt -export -out server.pfx
```

## combine req and crt in one command
```
...
```

## export csr from crt and key
```
#generate root ca
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
openssl x509 -noout -text -in server.crt

#export csr from crt and key
openssl x509 -x509toreq -in server.crt -signkey server.key -out new-server.csr
openssl req -noout -text -in new-server.csr #check server.csr    

#generate crt from key and new csr
openssl x509 -req -days 365 -in new-server.csr -signkey server.key -out new-server.crt -extfile v3.ext
sha256sum server.crt #verify server.crt   
```

## get issuer/subject
```
openssl x509 -noout -issuer -in cert.pem
openssl x509 -noout -subject -in ca.pem
```
