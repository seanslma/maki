# SSL tls

## command
```
openssl x509 -req -days 1000 -in tls.csr -signkey tls.key -out tls.crt -extfile v3.ext
```

## v3 extension
```
# OpenSSL configuration for v3 extension

#1.3.6.1.4.1.311.21.7 = ASN1:PRINTABLESTRING:0..&+.....x............./...{....&.......v..d...
extendedKeyUsage = serverAuth
keyUsage = digitalSignature, Key Encipherment
1.3.6.1.4.1.311.21.10 = ASN1:PRINTABLESTRING:0.0 #???
subjectKeyIdentifier = hash
subjectAltName = @alt_names
authorityKeyIdentifier = keyid, issuer
crlDistributionPoints = @crldp_section
#not working
authorityInfoAccess = caIssuers;URI:ldap:///CN=Example%20Certification%20Authority,CN=AIA,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=EXAMPLE,DC=com?cACertificate?base?objectClass=certificationAuthority

[ alt_names ]
DNS.1 = *.my.example.com
DNS.2 = *.dev.my.example.com

[ crldp_section ]
#fullname=URI: obsolete should not be used: https://www.mail-archive.com/openssl-users@openssl.org/msg55684.html
URI.1 = ldap:///CN=Example%20Certification%20Authority,CN=DC1PXXCS01,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=EXAMPLE,DC=com?certificateRevocationList?base?objectClass=cRLDistributionPoint

```
