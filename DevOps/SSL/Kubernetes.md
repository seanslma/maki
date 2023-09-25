# Kubernetes

## show cert details
```
openssl x509 -noout -text -in tls.crt
```

## validate cert
Will show server certificate details
```
curl https://my.example.com -kv
```

## kube ingress tls
The Kubernetes Secret and the Ingress controller must be in the same namepsace:
https://stackoverflow.com/questions/66469622/kubernetes-ingress-controller-not-able-to-find-the-certificate-secret

Not show the details about creating the cert

https://devopscube.com/configure-ingress-tls-kubernetes/

## kube certi 3 methods
https://kubernetes.io/docs/tasks/administer-cluster/certificates/

## kubernetes-ssl-certificates
https://phoenixnap.com/kb/kubernetes-ssl-certificates

## kubernetes-ssl/tls-certificates
https://medium.com/avmconsulting-blog/how-to-secure-applications-on-kubernetes-ssl-tls-certificates-8f7f5751d788

### Generate Certificate Files
produce a 2048-bit RSA encrypted key:
```
openssl genrsa -out ca.key 2048
```

use `ca.key` to generate `ca.crt`:
```
openssl req -x509 -new -nodes -key ca.key -subj "/CN=[my.example.com]" -days <ndays> -out ca.crt
```

generate `server.key` file with 2048-bit RSA encryption:
```
openssl genrsa -out server.key 2048
```

### Create Certificate Configuration File
generate certificate signing request (csr):
```
openssl req -new -key server.key -out server.csr -config csr.conf
```

`csr.conf`
```
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C = [country]
ST = [state]
L = [city]
O = [company]
OU = [organization-unit]
CN = [common-name]

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster
DNS.5 = kubernetes.default.svc.cluster.local
IP.1 = [MASTER_IP]
IP.2 = [MASTER_CLUSTER_IP]

[ v3_ext ]
authorityKeyIdentifier=keyid,issuer:always
basicConstraints=CA:FALSE
keyUsage=keyEncipherment,dataEncipherment
extendedKeyUsage=serverAuth,clientAuth
subjectAltName=@alt_names
```

### Generate the Certificate
create a server certificate `server.crt` with `ca.key`, `ca.crt` and `server.csr`
```
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out server.crt -days 1000 \
  -extensions v3_ext -extfile csr.conf
```

view the created certificate
```
openssl x509 -noout -text -in ./server.crt
```

##
https://kuberty.io/blog/how-to-generate-a-self-signed-certificate-for-kubernetes-2/
