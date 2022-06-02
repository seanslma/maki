# Kubernetes

kubectl Cheat Sheet:

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

https://unofficial-kubernetes.readthedocs.io/en/latest/user-guide/kubectl-cheatsheet/

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

## credential
```
az login #login
$env:KUBECONFIG="C:\Users\<user-name>\.kube\<your_aks_name>" # setup config in windows
az aks get-credentials --resource-group <aks-rg> --name <aks-name> --overwrite-existing #create credential
```

## job
```
kubectl -n <namespace> create job --from=cronjob/<crojob-name> <job-name> #create a job
kubectl -n <namespace> get job --sort-by=.status.startTime #show job status
```

## get pod info
```
kubectl describe pod <pod-name> -n <namespace>
```

## open a shell in a running pod container
```
kubectl exec -it <pod-name> -n <namespace> -- /bin/bash
kubectl exec -it <pod-name --container <container-name> -n <namespace> -- /bin/bash
```

## log
```
kubectl logs my-pod                                 #dump pod logs (stdout)
kubectl logs -l name=myLabel                        #dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod --previous                      #dump pod logs (stdout) for previous container
kubectl logs my-pod -c my-container                 #dump pod container logs (stdout, multi-container case)
kubectl logs -l name=myLabel -c my-container        #dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod -c my-container --previous      #dump pod container logs (stdout, multi-container case) for previous container
```

