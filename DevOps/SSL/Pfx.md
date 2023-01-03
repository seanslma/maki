# Pfx

## pfx to key and crt
```
openssl pkcs12 -in <filename.pfx> -nocerts -out <keyfilename-encrypted.key>
openssl pkcs12 -in <filename.pfx> -clcerts -nokeys -out <certificatename.crt>
openssl rsa -in <keyfilename-encrypted.key> -out <keyfilename-decrypted.key>
```

