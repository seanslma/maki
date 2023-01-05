# Intermediate CA

## Ordering certificate when using intermediates

When using intermediate certificate(s), we need to make sure that:
- the **application** using the certificate is sending the complete chain (`server` certificate and `intermediate` certificate). 
- and usually we have to create a file containing the `server` certificate file and the `intermediate` certificate file. 
- it is required to put the `server` certificate file first, and then the `intermediate` certificate file(s). 
- we can create the correct file for the chain using: `cat cert.pem intermediate.pem > chain.pem`
