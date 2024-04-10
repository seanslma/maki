# KubeAdm

## connect to k8s master (ubuntu)
```sh
ssh username@machine.example.com
```

## list images
```sh
kubeadm config images list
```

## sudo ls /etc/kubernetes/manifests/
- etcd.yaml
- kube-apiserver.yaml
- kube-controller-manager.yaml
- kube-scheduler.yaml

## CA path `/etc/kubernetes/pki`
The `apiserver-kubelet-client` is the client cert that API server will present to a kubelet.
check to determine that kubelet is configured to trust clients that are signed by the k8s CA `cat /var/lib/kubelet/config.yaml`.
```sh
$ sudo ls -al /etc/kubernetes/pki
total 68
drwxr-xr-x 3 root root 4096 Aug  5  2020 .
drwxr-xr-x 4 root root 4096 Aug  5  2020 ..
-rw-r--r-- 1 root root 1025 Aug  5  2020 ca.crt
-rw------- 1 root root 1679 Aug  5  2020 ca.key
drwxr-xr-x 2 root root 4096 Aug  5  2020 etcd
-rw-r--r-- 1 root root 1038 Aug  5  2020 front-proxy-ca.crt
-rw------- 1 root root 1679 Aug  5  2020 front-proxy-ca.key
-rw------- 1 root root 1675 Aug  5  2020 sa.key
-rw------- 1 root root  451 Aug  5  2020 sa.pub
-rw-r--r-- 1 root root 1220 Feb  1 11:08 apiserver.crt
-rw------- 1 root root 1679 Feb  1 11:08 apiserver.key
-rw-r--r-- 1 root root 1090 Feb  1 11:08 apiserver-etcd-client.crt
-rw------- 1 root root 1679 Feb  1 11:08 apiserver-etcd-client.key
-rw-r--r-- 1 root root 1099 Feb  1 11:08 apiserver-kubelet-client.crt
-rw------- 1 root root 1679 Feb  1 11:08 apiserver-kubelet-client.key
-rw-r--r-- 1 root root 1058 Feb  1 11:08 front-proxy-client.crt
-rw------- 1 root root 1675 Feb  1 11:08 front-proxy-client.key
```

`kubeadm alpha certs check-expiration` will check certs in `/etc/kubernetes/pki` and cert in `KUBECONFIG` file used by kubeadm（admin.conf, controller-manager.conf and scheduler.conf.

## cert path `/var/lib/kubelet/pki/kubelet.*`
```sh
$ sudo ls -al /var/lib/kubelet/pki
total 27
drwxr-xr-x 2 root root 4096 Mar 13  2023 .
drwx------ 8 root root 4096 Aug  5  2021 ..
-rw------- 1 root root 1070 May 20  2022 kubelet-client-2022-05-20-14-29-52.pem
-rw------- 1 root root 1070 Mar 10  2023 kubelet-client-2023-03-10-03-43-08.pem
lrwxrwxrwx 1 root root   59 Mar 10  2023 kubelet-client-current.pem -> /var/lib/kubelet/pki/kubelet-client-2022-03-10-03-43-08.pem
-rw-r--r-- 1 root root 2173 Aug  5  2021 kubelet.crt
-rw------- 1 root root 1679 Aug  5  2021 kubelet.key
```

## kubeadm-certs
https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs

https://www.chernsan.com/2021/02/09/etcd-certificates-expired/

Kubernetes certificates expire after one year.

kubeadm creates certs under `/var/lib/kubelet/pki/kubelet.*` signed with a different CA from the one under `/etc/kubernetes/pki/ca.pem`.

### check certs
```sh
kubeadm alpha certs check-expiration
kubeadm certs check-expiration        #new might not work
```

### renew certs
`kubelet.conf` will **not** be renewed by `kubeadm alpha certs renew all`.
```sh
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
```sh
cd ~/.kube
rm config.old
mv config config.old                      #archive old config
sudo cp /etc/kubernetes/admin.conf config #copy new config
sudo chown $(id -u):$(id -g) config       #aplly permissions to admin user and group
```

### copy the config file to all worker nodes
The updated `admin.conf` file should also be copied to `.kube/config` in all worker nodes with the right permissions being applied.

## do we need to do more to fix the issue?
https://serverfault.com/questions/1065444/how-can-i-find-which-kubernetes-certificate-has-expired

https://github.com/kubernetes/kubernetes/issues/102556

Kubeadm does not manage the kubelet cert rotation. It is automatic by default unless the user opts out.
