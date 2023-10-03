# KubeConfig

## show config path
run any kubectl command with verbose level 6+ to see the kubeconfig in use
```sh
kubectl get node -v6
```

## show config view
```sh
kubectl config view
```

## install kubectl on win
- copy file to your folder: https://dl.k8s.io/release/v1.25.0/bin/windows/amd64/kubectl.exe
- add the exe path to PATH var

## set config envvar
```sh
export KUBECONFIG="/mnt/c/users/usr/.config/.kube/config"
#default
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
export KUBECONFIG=$HOME/.kube/config
```

## modify config files
```sh
kubectl config view
kubectl config get-clusters
az aks get-credentials -n <aks-name> -g <resource-group-name>
kubectl config get-contexts
kubectl config unset users.usr
kubectl config delete-cluster <cluster-name>
kubectl config delete-context <cluster-name>
```

## merge kubeconfig files
```sh
cp ~/.kube/config ~/.kube/config.bak #make a copy
KUBECONFIG="~/.kube/config:~/.kube/config2" kubectl config view --flatten > /tmp/config #merge to a new file
mv /tmp/config ~/.kube/config #replace the config file
rm ~/.kube/config.bak #delete backup
```

## switch cluster
```sh
kubectl config get-contexts #display all contexts
kubectl config current-context #display current context
kubectl config use-context <cluster-name> #set default context
```
