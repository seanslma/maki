# KubeAPI

## check kube-api SSL cert
https://stackoverflow.com/questions/67132520/kubelet-service-cant-access-kube-apiserver-at-port-6443-with-https-due-to-error
```
curl -k -v https://172.24.4.159:6443
```

## connection was refused
https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552

https://www.reddit.com/r/kubernetes/comments/10aya7n/master_node_not_accessible_after_a_few_minutes

The connection to the server <ip>:6443 was refused - did you specify the right host or port?
- disable SWAP `swapoff -a`
- check if docker was running
- checked if kubelet was running, any log errors?
- disk is under 20GB but it is 100GB already
- reboot the master
- looking with netstat to see if something is running on port 6443
