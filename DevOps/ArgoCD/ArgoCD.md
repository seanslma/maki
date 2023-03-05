# ArgoCD
https://argoproj.github.io/

https://argo-cd.readthedocs.io/en/stable/operator-manual/

https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops

Argo CD provides Continuous Delivery tooling that automatically synchronizes and deploys applications whenever a change is made in GitHub repository.

## install ArgoCD to cluster
https://medium.com/@talhaaziz37/argo-cd-installation-in-kubernetes-kubeadm-ubuntu-lts-22-04-b429df6d4655
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
watch kubectl get pods -n argocd
```

## log to argocd ui
- use port-forward to expose a port to the service, and forward it to localhost
- get the login password (default user name is `admin`)
```
kubectl port-forward svc/argocd-server -n argocd 8080:443 # https://localhost:8080
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## argocd cli
```
#install argocd: https://argo-cd.readthedocs.io/en/stable/cli_installation
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64

#extract admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
argocd login localhost:8080
argocd account update-password

#handling multiple clusters
kubectl config get-contexts -o name
argocd cluster add target-k8s
```

## deploy app
```
argocd app create helm-guestbook --repo https://github.com/argoproj/argocd-example-apps.git --path helm-guestbook --dest-server https://kubernetes.default.svc --dest-namespace default
argocd app get helm-guestbook
argocd app sync helm-guestbook
```

## terraform
https://registry.terraform.io/providers/hashicorp/helm/latest/docs/resources/release

https://github.com/argoproj/argo-helm/tree/master/charts/argo-cd

https://www.bootiq.io/en/deploy-helm-charts-using-terraform-module
