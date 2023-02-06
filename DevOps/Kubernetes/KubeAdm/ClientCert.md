# Client Cert

## Kubelet client certificate rotation fails {#kubelet-client-cert}
https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/#kubelet-client-cert

https://github.com/kubernetes/website/blob/6ea53189723803c363d4de1c0cc76dd0cd98ff39/content/en/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubelet-client-certificate-rotation-fails-kubelet-client-cert

By default, kubeadm configures a kubelet with automatic rotation of client certificates by using 
the /var/lib/kubelet/pki/kubelet-client-current.pem symlink specified in /etc/kubernetes/kubelet.conf. 
If this rotation process fails you might see errors such as x509: certificate has expired or is not yet valid in kube-apiserver logs. 

To fix the issue you must follow these steps:
- Backup and delete /etc/kubernetes/kubelet.conf and /var/lib/kubelet/pki/kubelet-client* from the failed node.
- From a working control plane node in the cluster that has /etc/kubernetes/pki/ca.key
  execute kubeadm kubeconfig user --org system:nodes --client-name system:node:$NODE > kubelet.conf. 
  $NODE must be set to the name of the existing failed node in the cluster. 
  Modify the resulted kubelet.conf manually to adjust the cluster name and server endpoint, or pass kubeconfig user --config (it accepts InitConfiguration). 
  If your cluster does not have the ca.key you must sign the embedded certificates in the kubelet.conf externally.
- Copy this resulted kubelet.conf to /etc/kubernetes/kubelet.conf on the failed node.
- Restart the kubelet (systemctl restart kubelet) on the failed node and wait for /var/lib/kubelet/pki/kubelet-client-current.pem to be recreated.
- Manually edit the kubelet.conf to point to the rotated kubelet client certificates, by replacing client-certificate-data and client-key-data with:
  ```
  client-certificate: /var/lib/kubelet/pki/kubelet-client-current.pem
  client-key: /var/lib/kubelet/pki/kubelet-client-current.pem
  ```
- Restart the kubelet.
- Make sure the node becomes Ready.
