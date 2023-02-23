# Cert

## argocd-tls-cert-cm
cert can be installed in `argocd-tls-cert-cm`:
https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/

## Connect to private repo
https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#repositories

https://argo-cd.readthedocs.io/en/release-1.8/user-guide/private-repositories/

**Error**: `Unable to deploy revision: rpc error: code = Unknown desc = authentication required`
Solution:
- settings > repositories > connecting repo using https > url and pat

**Error**: ` x509: certificate signed by unknown authority`
Solution:
- add the server's certificate, or the certificate of the CA used to sign the server's certificate to `argocd-tls-cert-cm`.
