# kube-apiserver

## cluster info
detailed information about the overall health of the cluster
```sh
kubectl cluster-info
kubectl cluster-info dump
```

## check kube-apiserver is running and hasn't crashed
https://discuss.kubernetes.io/t/the-connection-to-the-server-localhost-8080-was-refused-did-you-specify-the-right-host-or-port/1464/3
```sh
docker ps | grep kube-apiserver
```

## check kube-apiserver SSL cert
https://stackoverflow.com/questions/67132520/kubelet-service-cant-access-kube-apiserver-at-port-6443-with-https-due-to-error
```sh
curl -kv https://172.24.4.159:6443
```

## check kube-apiserver health
https://kubernetes.io/docs/reference/using-api/health-checks/
```sh
curl -k https://localhost:6443/livez?verbose
```

## Why disable swap on kubernetes
https://serverfault.com/questions/881517/why-disable-swap-on-kubernetes

- Support for swap is non-trivial.
- Guaranteed pods should never require swap.
- Burstable pods should have their requests met without requiring swap.
- BestEffort pods have no guarantee.
- The kubelet right now lacks the smarts to provide the right amount of predictable behavior here across pods.

## The connection to the server ip:6443 was refused - did you specify the right host or port?
https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552

https://www.reddit.com/r/kubernetes/comments/10aya7n/master_node_not_accessible_after_a_few_minutes

- certs expired
  ```sh
  kubeadm alpha certs check-expiration
  ```
- has config setup correctly?
  ```sh
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
  export KUBECONFIG=$HOME/.kube/config
  ```
- disable SWAP `swapoff -a`
  ```sh
  #to make it permanent go to /etc/fstab
  sudo -i
  swapoff -a
  exit
  strace -eopenat kubectl version
  sudo systemctl restart kubelet.service
  ```
  further steps?
  ```sh
  #remove the && and \ and copy and paste each line in the command line, this will ensure swap is disabled and persistent across a reboot.
  sudo dphys-swapfile swapoff && \
  sudo dphys-swapfile uninstall && \
  sudo systemctl disable dphys-swapfile
  ```
- check if docker was running
- checked if kubelet was running, any log errors?
- disk is under 20GB but it is 100GB already `df -H`
- reboot the master
- firewall blocks the port
  ```sh
  sudo systemctl status firewalld #redhat centos
  sudo systemctl stop firewalld #redhat, centos
  sudo ufw status verbose #ubuntu
  sudo ufw disable #ubuntu
  ```
- looking with netstat to see if something is running on port 6443
- `kubeadm reset` on master and worker nodes?
