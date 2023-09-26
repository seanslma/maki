# Ingress TSL
how to update kubernetes ingress tsl

## generate self signed tls

## Extract certificate key pair
Self signed certificate in pfx format is usually stored in the Azure Key-vault Certificates store.
A Kubernetes Secret can be created directly in terraform to load the cert from Azure Key-vault.

The pfx cert include both the private key and certificate. 
Use the following commands to extract the key pair (tls.key and tls-raw.crt) from the pfx file:
```sh
openssl pkcs12 -in tls.pfx -nocerts -out tls-encrypted.key
openssl pkcs12 -in tls.pfx -clcerts -nokeys -out tls-raw.crt
openssl rsa -in tls-encrypted.key -out tls.key
```
Note that when extracting the key pair, a passphrase is required which should be recorded when generating the cert.
The tls.crt file should include all level (local, intermediate, and root from top to bottome) certificate files in the chain. 
After downloading the CA certificates from the web browser, run the following commands to concatenation the certificates to one file:
```sh
cp tls-raw.crt tls.crt
cat intermediate-ca.crt >>tls.crt
cat root-ca.crt >>tls.crt
```

## Update server certificate in Kubernetes
In the Kubernetes cluster, the server certificate key pair is installed into the cluster Secrets store for the `traefik` ingress controller application. 
To directly update the key pair in the cluster, run
```sh
key=$(base64 < "./tls.key" | tr -d '\n')
crt=$(base64 < "./tls.crt" | tr -d '\n')
kubectl patch secret tls-cert -n traefik \
    -p "{\"data\":{\"tls.key\":\"${key}\",\"tls.crt\":\"${crt}\"}}"
```
