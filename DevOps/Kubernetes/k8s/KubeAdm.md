# KubeAdm

## connect to k8s master (ubuntu)
```
ssh username@machine.example.com
```

## sudo ls /etc/kubernetes/manifests/
- etcd.yaml  
- kube-apiserver.yaml  
- kube-controller-manager.yaml  
- kube-scheduler.yaml

## kubeadm-certs
https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs

https://www.chernsan.com/2021/02/09/etcd-certificates-expired/

Kubernetes certificates expire after one year.

### check certs
```
kubeadm alpha certs check-expiration
kubeadm certs check-expiration        #new might not work
```

### renew certs
```
#do we need this before renewal?
kubeadm init phase kubelet-finalize all #'symlink' kebelet.conf to kubelet cert rotation

kubeadm alpha certs renew all           #renew all certs
kubeadm alpha certs renew <CERTIFICATE> #renew one cert
kubeadm certs renew <CERTIFICATE>       #new might not work

#do we need this after renewal?
cd /etc/kubernetes
kubeadm alpha kubeconfig user --org system:nodes --client-name system:node:$(hostname) > kubelet.conf
```

### update config
https://www.oak-tree.tech/blog/k8s-cert-yearly-renewwal
```
cd ~/.kube
rm config.old
mv config config.old                      #archive old config
sudo cp /etc/kubernetes/admin.conf config #copy new config
sudo chown $(id -u):$(id -g) config       #aplly permissions to admin user and group
```

## do we need to do more to fix the issue?
https://serverfault.com/questions/1065444/how-can-i-find-which-kubernetes-certificate-has-expired

https://github.com/kubernetes/kubernetes/issues/102556

Kubeadm does not manage the kubelet cert rotation. It is automatic by default unless the user opts out.
