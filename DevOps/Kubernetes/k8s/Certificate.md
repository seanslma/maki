# Certificate

https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

## Control plane automated approval
```
#get the list of CSRs
kubectl get csr -A

#approve a CSR with kubectl
kubectl certificate approve <csr-name>

#deny a CSR
kubectl certificate deny <csr-name>
```

## get-a-certificate-signing-request-every-15-minutes
https://serverfault.com/questions/1112910/i-get-a-certificate-signing-request-every-15-minutes-kubernetes

starting the management cluster!
