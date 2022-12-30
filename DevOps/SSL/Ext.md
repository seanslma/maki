# Extension

## x509 Extensions for different types of certificates
https://www.golinuxcloud.com/add-x509-extensions-to-certificate-openssl/

## x509v3 config
https://www.openssl.org/docs/man1.0.2/man5/x509v3_config.html
```
extendedKeyUsage=serverAuth
keyUsage=digitalSignature, Key Encipherment
subjectKeyIdentifier=hash
subjectAltName=DNS:*.my.example.com, DNS:*.dev.my.example.com
authorityKeyIdentifier=keyid,issuer
authorityInfoAccess=caIssuers;URI:http://my.ca/ca.html
crlDistributionPoints=crldp1_section

[crldp1_section]

fullname=URI:http://myhost.com/myca.crl

certificatePolicies=1.2.4.5, 1.1.3.4
```

## Key usage
https://superuser.com/questions/738612/openssl-ca-keyusage-extension

## CRL distribution points
https://security.stackexchange.com/questions/226242/where-do-you-get-the-digicert-crl-distribution-point
- Root certificates do not include a CRL (Certificate Revocation List) distribution point, because root certificates cannot be revoked.
- The CRL distribution point URL is included in (all) certificates issued by that root certificate.

Purpose
- The CR is a cryptographically signed list that contains the serial number of revoked certificates issued by that particular root or intermediate CA.
- Browsers nowadays do no longer use the CRL to check for revoked certificates, instead they rely on a mechanism called OCSP or OCSP Stapling.
- Some browsers also ship their own list of revoked certificates with every browser update (e.g. OneCRL from Mozilla).
- Other software, like Microsoft Windows, still fetches, caches and honors CRLs.

https://stackoverflow.com/questions/11966123/howto-create-a-certificate-using-openssl-including-a-crl-distribution-point

You can get the crlDistributionPoints into your certificate in (at least) these two ways:
- Use openssl ca rather than x509 to sign the request. Pass -config as needed if your config is not in a default location. Most of your provided command can be used if you omit the options starting with -CA
```
openssl ca -in $NAME.csr -out certs/$NAME.pem -days 3650
```
- Use the command as you've provided in your question, but first create a file containing your v3 extensions (ie mycrl.cnf); add the option -extfile mycrl.cnf to your call to openssl x509
```
openssl x509 -req -in $NAME.csr -out certs/$NAME.pem -days 3650 \
  -CAcreateserial -CA cacert.pem -CAkey private/cakey.pem \
  -CAserial serial -extfile mycrl.cnf
```
Where mycrl.cnf contains the following:
```
crlDistributionPoints=URI:http://example.com/crl.pem
```

## Issue different from subject
https://stackoverflow.com/questions/21666516/openssl-how-do-i-set-the-issuer-details

See this example: https://pages.cs.wisc.edu/~zmiller/ca-howto/
