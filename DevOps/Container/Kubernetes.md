# Kubernetes

Container orchestration tool.

https://github.com/kelseyhightower/intro-to-kubernetes-workshop/blob/master/labs/cluster-add-on-ui.md


## install kubectl on wsl2
```
# kubectl will be installed in `/usr/local/bin/kubectl`
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.22.8/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

# open file ~/.profile update the path for kubectl, also add
export KUBECONFIG=/mnt/c/users/$WindowsUSER/.kube/kube_config_filename

# Reopen wsl2 to re-read .profle file
```
