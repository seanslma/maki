# Kubernetes

kubectl commands:

https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec

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

## kubectl cheatsheet
https://unofficial-kubernetes.readthedocs.io/en/latest/user-guide/kubectl-cheatsheet/

## kubectl basic
```
#login
az login
# setup config in windows
$env:KUBECONFIG="C:\Users\<user-name>\.kube\<your_aks_name>"
# create credential
az aks get-credentials --resource-group <aks-rg> --name <aks-name>
# create a job, last one is the name
kubectl -n <namespace> create job --from=cronjob/<crojob-name> <job-name>
# show job status
kubectl -n <namespace> get job --sort-by=.status.startTime
# show logs
kubectl logs
```
