# Certificate

https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

Kubernetes can be configured to certificate rotation. 
However, there are cases the certificate rotation does not work. In this situation, we need to check and renew the certificates manually.

If not mentioned specifically, all the following commands are executed in the k8s master node.

## Cert types
There are two types of certs in kubernetes
- `kubeadm` for master、etcd: renew via `kubeadm alpha certs renew all`
- `kubelet` for kubelet: connection between node and master (usually 1 year expiration)

## check certs
https://serverfault.com/questions/1068751/var-lib-kubelet-pki-kubelet-crt-is-expired-how-to-renew-it

check `/var/lib/kubelet/pki/kubelet.crt`, or really for the certificate signed by the kube-apiserver, not specifically the kubeadm or kubectl certificates?
```sh
echo -n | openssl s_client -connect localhost:10250 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | openssl x509 -text -noout | grep -A 2 Validity
```

why this command gave the wrong info?
```sh
sudo openssl x509 -in /var/lib/kubelet/pki/kubelet.crt -text -noout  | grep -A 2 Validity
```

## Enabling signed kubelet serving certificates
https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/

If you have already created the cluster you must adapt it by doing the following:
- Find and edit the `kubelet-config-1.xx` ConfigMap in the kube-system namespace.
  In that ConfigMap, the kubelet key has a KubeletConfiguration document as its value.
  Edit the KubeletConfiguration document to set `serverTLSBootstrap: true`.
- On each node, add the `serverTLSBootstrap: true` field in `/var/lib/kubelet/config.yaml` and restart the kubelet with `systemctl restart kubelet`.

## Certificate rotation (auto renewal) settings
- https://kubernetes.io/docs/tasks/tls/certificate-rotation/
- https://github.com/kubernetes/kubeadm/issues/2024

https://www.leiyawu.com/2020/10/11/Untitled/
- from v1.8, to auto reload certs when start kubelet add option `–rotate-certificates`
- kubelet auto renew certs, when start add `–feature-gates=RotateKubeletClientCertificate=true,RotateKubeletServerCertificate=true`
- controller manager auto approve CSRs, when start add `–feature-gates=RotateKubeletServerCertificate=true` and bind RBAC rules

If the certificate rotation is not enabled or not setup correctly, we should check and setup the configuration.

After enable the rotation `/var/lib/kubelet/pki/kubelet.crt` is no longer used, 
instead the symbolic link `/var/lib/kubelet/pki/kubelet-server-current.pem` is used and points to the latest rotated certificate.

### config kubelet
Make sure the following options are in `/var/lib/kubelet/config.yaml`
```yaml
rotateCertificates: true #enable client cert rotation
serverTLSBootstrap: true #enable server cert rotation
featureGates:
  RotateKubeletClientCertificate: true
  RotateKubeletServerCertificate: true
```
```
--rotate-certificates
--feature-gates=RotateKubeletClientCertificate=true
--feature-gates=RotateKubeletServerCertificate=true
```

### config kube-controller-manager 
Make sure the folowing options are in `/etc/kubernetes/manifests/kube-controller-manager.yaml`
```yaml
spec:
  containers:
  - command:
    - --experimental-cluster-signing-duration=17520h0m0s  #2 years
    - --feature-gates=RotateKubeletClientCertificate=true,RotateKubeletServerCertificate=true #auto approve csr
```

### Create Server ClusterRole and ClusterRoleBinding
**system:certificates.k8s.io:certificatesigningrequests:selfnodeserver**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: system:certificates.k8s.io:certificatesigningrequests:selfnodeserver
rules:
- apiGroups:
  - certificates.k8s.io
  resources:
  - certificatesigningrequests/selfnodeserver
  verbs:
  - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubeadm:node-autoapprove-certificate-server
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:certificates.k8s.io:certificatesigningrequests:selfnodeserver
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:nodes
```
create ClusterRole `kubectl apply -f ca-update.yaml`.
show all ClusterRoles `k get ClusterRole -A`.

We can also create the ClusterRoleBinding using cli:
**certificatesigningrequests:selfnodeserver**: auto renew certs for `kubelet 10250 api` in `system:nodes` group
```sh
kubectl create clusterrolebinding kubeadm:node-autoapprove-certificate-server \
  --clusterrole=system:certificates.k8s.io:certificatesigningrequests:selfnodeserver --group=system:nodes
```
Included in `ca-update.yaml`.

### Create Client ClusterRoleBinding
**certificatesigningrequests:nodeclient**: auto approve TLS bootstrapping first request by `kubelet-bootstrap` users
```sh
kubectl create clusterrolebinding kubeadm:node-autoapprove-bootstrap \
  --clusterrole=system:certificates.k8s.io:certificatesigningrequests:nodeclient --user=kubelet-bootstrap
```

**certificatesigningrequests:selfnodeclient**: auto renew certs for `kubelet` and `apiserver` in `system:nodes` group
```sh
kubectl create clusterrolebinding kubeadm:node-autoapprove-certificate-rotation \
  --clusterrole=system:certificates.k8s.io:certificatesigningrequests:selfnodeclient --group=system:nodes
```

**Edit kubelet-config-1.xx**
```sh
k get cm -A
kubectl edit configmap -n <namespace> <config-map-name> -o yaml
```

**Restart** `kube-controller-manager` and `kubelet` services
```sh
#restart controller-manager
systemctl restart kube-controller-manager

#delete kubelet certs in ssl
rm -f kubelet-client-current.pem kubelet-client-2021-05-10-09-45-21.pem kubelet.key kubelet.crt

#restart kubelet, new certs will be renewed
systemctl restart kubelet

#check renewed certs
openssl x509 -noout -text -in kubelet-client-current.pem | grep "Not"
```

## Control plane approval
`journalctl -xeu kubelet -n 100 --no-pager`
error: no serving certificate available for the kubelet
```sh
#get the list of CSRs
kubectl get csr -A

#approve a CSR with kubectl
kubectl certificate approve <csr-name>

#deny a CSR
kubectl certificate deny <csr-name>
```

## manually approve all pending CSRs
If there are errors like `error: no serving certificate available for the kubelet from journalctl -xeu kubelet -n 100 --no-pager`, run
```sh
kubectl get csr -A | grep Pending | awk '{print $1}' | xargs kubectl certificate approve
kubectl get csr -A | grep Pending | tr -s ' ' | cut -d' ' -f1 | while IFS= read -r csr; do kubectl certificate approve $csr; done
```

## get-a-certificate-signing-request-every-15-minutes
https://serverfault.com/questions/1112910/i-get-a-certificate-signing-request-every-15-minutes-kubernetes

kubelet log:
certificate_manager.go:451] certificate request was not signed: timed out waiting for the condition

kubernetes CSR in pending status
```sh
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
