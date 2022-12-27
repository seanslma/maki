# SSL Ext

## DigiCert CRL (Certificate Revocation List) distribution point
https://security.stackexchange.com/questions/226242/where-do-you-get-the-digicert-crl-distribution-point
- Root certificates do not include a CRL distribution point, because root certificates cannot be revoked.
- The CRL distribution point URL is included in (all) certificates issued by that root certificate. 

Purpose
- The CR is a cryptographically signed list that contains the serial number of revoked certificates issued by that particular root or intermediate CA. 
- Browsers nowadays do no longer use the CRL to check for revoked certificates, instead they rely on a mechanism called OCSP or OCSP Stapling. 
- Some browsers also ship their own list of revoked certificates with every browser update (e.g. OneCRL from Mozilla). 
- Other software, like Microsoft Windows, still fetches, caches and honors CRLs.
