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
