# Docker

## x509: certificate signed by unknown authority
After adding the tls.crt to the path `/etc/ssl/certs` or `/usr/local/share/ca-certificates` and run `update-ca-certificates`.
The command `curl -kv https://my.example.com` shows `SSL certificate verify ok` but docker build shows `x509: certificate signed by unknown authority`.

solution: https://stackoverflow.com/questions/50768317/docker-pull-certificate-signed-by-unknown-authority

After updating OS certificates, we typically need to restart the docker service to get it to detect that change. 
This is usually done with:
```sh
sudo systemctl restart docker
```
or for non-systemd environments:
```sh
sudo service docker restart
```

## Why not include leaf cert in trust store
Note: If it's self-asigned as the root ca is itself, we should include it.

In most cases, especially for environments like Azure Kubernetes Service, we should NOT add a leaf certificate (e.g. `*.example.com`) to the trust store.

### Purpose of root/intermediate and leaf certs
A **trust store** is meant to contain **Certificate Authority (CA) certificates**, not end-entity (leaf) certificates.

**CA certificates (root or intermediate)**:
- Used to **verify** other certificates
- Belong in the trust store

**Leaf certificates (`*.example.com`)**:
- Issued *by* a CA to a service
- Used to **identify a server**, not to establish trust

### Issues by adding a leaf cert
If we add something like `*.example.com` to the trust store:
- We're effectively saying: "Trust this exact certificate as a root authority"
- This **bypasses proper certificate chain validation**
- It can introduce **security risks**, because:
  - Expiry/rotation becomes fragile
  - We lose proper issuer verification
  - It breaks standard TLS trust logic

### Correct way to do it
Inside an AKS pod (or any container):
- Add the **root CA** or **intermediate CA** that issued the certificate
- Let TLS verify the full chain normally

Typical flow:
- Server presents the leaf cert (`*.example.com`) and intermediate(s)
- The pod trusts the **CA** and validates the chain (secure connection)
