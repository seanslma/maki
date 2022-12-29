# SSl ca

## create key
```
openssl genrsa -out ca_test.key 2048
```

## create crt
```
openssl req -new -x509 -days 365 -key ca_test.key -out ca_test.crt -config ca.cnf
```

## ca.cnf
```
# OpenSSL configuration for Root CA

oid_section = oids

[ oids ]
certificateTemplate     = 1.3.6.1.4.1.311.20.2
caVersion               = 1.3.6.1.4.1.311.21.1
certificateTemplateName = 1.3.6.1.4.1.311.21.2

[ req ]
prompt             = no
string_mask        = default

default_bits       = 2048
distinguished_name = req_distinguished_name
x509_extensions    = x509_ext

[ req_distinguished_name ]
DC   = com
1.DC = Example
CN   = Example Certification Authority

[ x509_ext ]
certificateTemplate     = ASN1:BMP:CA
keyUsage                = digitalSignature, keyCertSign, cRLSign
basicConstraints        = critical, CA:true
subjectKeyIdentifier    = hash
caVersion               = ASN1:INTEGER:0
certificateTemplateName = ASN1:PRINTABLESTRING:X?......o.....5K...c
#certificateTemplateName = ASN1:BMP:EXAMPLE-CA
```
