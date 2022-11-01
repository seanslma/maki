# ArgoCD

https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops

## Connect to private repo
https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#repositories

https://argo-cd.readthedocs.io/en/release-1.8/user-guide/private-repositories/

Error:
- Unable to deploy revision: rpc error: code = Unknown desc = authentication required

Solution:
- settings > repositories > connecting repo using https > url and pat

## install ArgoCD
https://medium.com/@talhaaziz37/argo-cd-installation-in-kubernetes-kubeadm-ubuntu-lts-22-04-b429df6d4655
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl get pod -n argocd
kubectl -n argocd port-forward svc/argocd-server 8080:443
kubectl -n agrocd get secret argocd-initial-admin-secret -o yaml #Admin
```
