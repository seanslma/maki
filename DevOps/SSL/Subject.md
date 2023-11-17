# Subject

## Common Name (will be depreciated)
The Common Name (CN) represents the server name protected by the SSL certificate. 
The certificate is valid only if the request hostname matches the certificate common name. 
Most web browsers display a warning message when connecting to an address that does not match the common name in the certificate.

### CN = exemple.com
This cert will only be valid for domain `exemple.com`

### CN = exemple.com CN = *.exemple.com
In this case the cert will be valid for the domain `exemple.com` and all subdomains such as `blog.example.com`.

It does not matter whether the SN has the star or not. The DNS should include both.

## Subject Alternative Name
The Subject Alternative Name (SAN) is an extension to the X.509 specification that allows users to specify additional host names for a single SSL certificate. 
The use of the SAN extension is standard practice for SSL certificates, and it’s on its way to replacing the use of the common name (CN).
