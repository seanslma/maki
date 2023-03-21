# Kubectl
https://kubernetes.io/docs/reference/kubectl/

## install
https://kubernetes.io/docs/tasks/tools/
```
curl -LO https://dl.k8s.io/release/v1.24.9/bin/windows/amd64/kubectl.exe

curl -LO https://dl.k8s.io/release/v1.24.9/bin/linux/amd64/kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

https://github.com/Azure/kubelogin
```
export KUBECONFIG=/path/to/kubeconfig
kubelogin convert-kubeconfig
kubectl get no
```

## show all info
```
kubectl get node -v=7
kubectl get node -v=10
```

## list all resources in a namespace
```
kubectl get all -n <namespace> #not list all

kubectl api-resources --verbs=list --namespaced -o name \
  | xargs -n 1 kubectl get --show-kind --ignore-not-found -n <namespace>
```
