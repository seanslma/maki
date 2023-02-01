# KubeAdm

## connect to k8s master (ubuntu)
```
ssh username@machine.example.com
```

## certs info
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
kubeadm alpha certs renew all           #renew all certs
kubeadm alpha certs renew <CERTIFICATE> #renew one cert
kubeadm certs renew <CERTIFICATE>       #new might not work
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
