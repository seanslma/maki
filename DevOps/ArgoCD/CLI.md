# CLI

## argocd cli
```sh
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

## add repo
```sh
argocd repo add acrxxxxxx.azurecr.io/helm --type helm --name acrxxxx --enable-oci \
--username argocd-creds --password "oJwFNBGsC1qnL2y+calxp/TmuhkhDmFD0Jhnxxxxxxxxxx" --upsert
```

## deploy app
```sh
argocd app create helm-guestbook --repo https://github.com/argoproj/argocd-example-apps.git \
--path helm-guestbook --dest-server https://kubernetes.default.svc --dest-namespace default
argocd app get helm-guestbook
argocd app sync helm-guestbook
```
