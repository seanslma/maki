# Cert
https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/

https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#repositories

ArgoCD uses certs (public and private keys) to connect to private repos.

## add cert into `argocd-tls-cert-cm`
https://github.com/argoproj/argo-cd/issues/6048

https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#repositories-using-self-signed-tls-certificates-or-are-signed-by-custom-ca

The certs should be added in the values.yaml file
```
configs:
  repositories:
    my-repo:
      url: https://my.example.com/repo
  tlsCerts:
    data:
      my.example.com: |
        -----BEGIN CERTIFICATE-----
        xx...yy
        -----END CERTIFICATE-----
```
The certificates are propagated through a volume mount of the `argocd-tls-certs-cm` ConfigMap.
If the cert is added, at `/app/config/tls` in the `argocd-repo-server` pod there should be a file named like the repo server.

Argo CD uses a kind of certificate pinning - that means, each certificate is pinned to the **name** of the repository server, and must be configured accordingly.

## Connect to private repo
**Error**: `Unable to deploy revision: rpc error: code = Unknown desc = authentication required`
Solution:
- settings > repositories > connecting repo using https > url and pat

**Error**: ` x509: certificate signed by unknown authority`
Solution:
- add the server's certificate, or the certificate of the CA used to sign the server's certificate to `argocd-tls-cert-cm`.
- test it `helm repo add jh https://example.com/jupyterhub --ca-file /app/config/tls/my.crt`

## issue for private helm chart repo with self-signed cert
https://github.com/argoproj/argo-cd/issues/9607
- create new argocd image: add cert to `/usr/local/share/ca-certificates/` and update `update-ca-certificates`
- mount the tls certificates from argocd's config-map into the default ssl certificate folder of golang's http client
  ```
  applicationSet:
    extraVolumeMounts:
    - name: certificates
      mountPath: /etc/ssl/certs/cert1.crt
      subPath: cert1.crt
  ```
 - use insecure option
  ```
  name: private-repo
  type: helm
  insecure: true
  url: https://private-repo.com
  ```

## x509: certificate signed by unknown authority
https://github.com/argoproj/argo-cd/issues/6048

The `ssh-known-hosts` and `tls-certs` ConfigMaps need to be mounted to the argocd-repo-server pods.
```sh
kubectl -n argocd describe deployments.apps argocd-repo-server 
```
