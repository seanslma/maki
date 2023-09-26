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
### check the cert works or not
- do not use a webbrowser - there is cache and delay - not reliable
- use `curl -kv https:example.com`
### check the ingress controller logs
The ingress should be integrated with one of the ingress controller (traefik, nginx, and ?). check the log of the ingress controller pod logs.
### tls: private key does not match public key
Used the wrong public key or the server public key is not placed in the file first (should be server, intermediate, root keys)
### Skipping addition of certificate for domain(s) \"example.com,*.example.com\", to EntryPoint https, as it already exists for this Entrypoint
- run `curl -kv https://dev.example.com` and still get the old certificate.
  Restart the ingress controller pods (some report indicates that the old cert can still be used) and check the pod logs, 
- `Error configuring TLS for ingress dev/sales-api: secret dev/example.com-tls-cert does not exist`.
  Updated the Secret with the same name in another namespace but not in the ingress controller namespace.

## Install root and intermediate CA files for dev.example.com domain
For self-signed certificate in the certificate chain, both the root and intermediate CA files 
should be installed in the certificate trust store to avoid the error `self signed certificate in certificate chain`.

In the docker base image:
- First add all the new certificate files into the docker folder.
- Then update the base.docker file add `COPY root-ca.crt intermediate-ca.crt /usr/local/share/ca-certificates/extra/` and `RUN update-ca-certificates`.
- At last, make a new release of the base and rebuild all applications using this new base image.

Question: can we map the cert files to a volume so we do not need to update the docker image after cert renewal? what's the prons and cons?
