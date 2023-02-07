# Auth

## Kubernetes client API error 401 - Unauthorized
add configuration to cluster config
```
kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts
```

## You must be logged in to the server (the server has asked for the client to provide credentials)
maybe due to issues in `.kube/config` file

## The connection to the server xx.xx.xx.xx:port was refused - did you specify the right host or port?
Possible reasons
- config not set: `export KUBECONFIG=$HOME/.kube/config`
- certs expired

## Kubectl connect: connection refused
detailed steps to check the issues:
https://medium.com/@texasdave2/troubleshoot-kubectl-connection-refused-6f5445a396ed

## kube-apiserver log, but certs are renewed
Unable to authenticate the request due to an error apiserver x509: certificate has expired or is not yet valid

**solution**: after cert renewal restart the master node

### check component status
```
kubectl get componentstatuses
```

### check ports
```
sudo netstat -lnpt | grep kube
netstat -a | grep 6443
```

### check firewall
```
#ubuntu
sudo ufw status verbose
sudo ufw disable
sudo ufw enable
#make sure kube-apiserver can get through port 6443
sudo ufw allow 6443/tcp
#try telnet from another host to your apiserver
telnet MASTER-IP 6443
```

### check kubeconfig file
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

cd .kube
ls -la
```

### check master node server address that kubectl running from
```
ifconfig
cat config
```

### restart kubelet 
```
### do not do this on a dev or production install
sudo systemctl stop kubele

sudo systemctl start kubelet
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### restart docker
```
sudo systemctl stop docker
sudo systemctl start docker
```
