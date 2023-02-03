# Certificate

https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

## Cert types
There are two types of certs in kubernetes
- for master、etcd
- for kubelet: connection between node and master (usually 1 year expiration)

## Certs auto renewal settings
https://www.leiyawu.com/2020/10/11/Untitled/
- kubelet auto renew certs, when start add `–feature-gates=RotateKubeletClientCertificate=true,RotateKubeletServerCertificate=true`
- controller manager auto approve CSRs, when start add `–feature-gates=RotateKubeletServerCertificate=true` and bind RBAC rules
- from v1.8, to auto reload certs when start kubelet add option `–rotate-certificates`
kubelet config
```
--feature-gates=RotateKubeletServerCertificate=true
--feature-gates=RotateKubeletClientCertificate=true
--rotate-certificates
```
controller-manager config (10 years)
```
--experimental-cluster-signing-duration=87600h0m0s
--feature-gates=RotateKubeletServerCertificate=true
```

## Control plane automated approval
```
#get the list of CSRs
kubectl get csr -A

#approve a CSR with kubectl
kubectl certificate approve <csr-name>

#deny a CSR
kubectl certificate deny <csr-name>
```

## manually approve all pending CSRs
```
kubectl get csr -A | grep Pending | tr -s ' ' | cut -d' ' -f1 | while IFS= read -r csr; do kubectl certificate approve $csr; done
```

## get-a-certificate-signing-request-every-15-minutes
https://serverfault.com/questions/1112910/i-get-a-certificate-signing-request-every-15-minutes-kubernetes

kubelet log: 
certificate_manager.go:451] certificate request was not signed: timed out waiting for the condition

kubernetes CSR in pending status
```
user@example:$ k get csr -A
NAME        AGE     SIGNERNAME                                    REQUESTOR               CONDITION
csr-2444s   13h     kubernetes.io/kube-apiserver-client-kubelet   system:node:node1       Pending
```
`kubernetes.io/kube-apiserver-client-kubelet`: signs client certificates that will be honored as client certificates by the API server. 
May be auto-approved by `kube-controller-manager`.

starting the management cluster!

## auto approval for server CSRs was removed
https://github.com/kubernetes/kubernetes/issues/73356

The CSR approving controllers implemented in core Kubernetes do **not** approve node serving certificates for security reasons. To use RotateKubeletServerCertificate operators need to run a custom approving controller, or manually approve the serving certificate requests.
