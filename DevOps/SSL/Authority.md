# Authority

## Authority Info Access with comma
https://mta.openssl.org/pipermail/openssl-users/2021-January/013291.html

put the uri in another section
```
authorityInfoAccess = @v3_aia

[ v3_aia ]
caIssuers;URI=ldap:///CN=Example%20Certification%20Authority,CN=AIA,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=EXAMPLE,DC=com?cACertificate?base?objectClass=certificationAuthority
```
