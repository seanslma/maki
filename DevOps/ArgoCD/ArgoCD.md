# ArgoCD
https://argoproj.github.io/

https://argo-cd.readthedocs.io/en/stable/operator-manual/

https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops

https://levelup.gitconnected.com/getting-started-with-argocd-on-your-kubernetes-cluster-552ca5d8cf41

Argo CD provides Continuous Delivery tooling that automatically synchronizes and deploys applications whenever a change is made in GitHub repository.

## install ArgoCD to cluster
https://medium.com/@talhaaziz37/argo-cd-installation-in-kubernetes-kubeadm-ubuntu-lts-22-04-b429df6d4655
```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
watch kubectl get pods -n argocd
```

## log to argocd ui
- use port-forward to expose a port to the service, and forward it to localhost
- get the login password (default user name is `admin`)
```sh
kubectl port-forward svc/argocd-server -n argocd 8080:443 # https://localhost:8080
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Also can deploy a NodePort service for ArgoCD so we do not need `port-forward`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: argocd-server-nodeport
  namespace: argocd
  labels:
    app.kubernetes.io/component: server
    app.kubernetes.io/name: argocd-server
    app.kubernetes.io/part-of: argocd
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: argocd-server
  ports:
    - name: http
      port: 80
      protocol: TCP
      targetPort: 8080
      nodePort: 30007
    - name: https
      port: 443
      protocol: TCP
      targetPort: 8080
      nodePort: 30008
  sessionAffinity: None
```

## project and application
https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/

## terraform
https://registry.terraform.io/providers/hashicorp/helm/latest/docs/resources/release

https://github.com/argoproj/argo-helm/tree/master/charts/argo-cd

https://www.bootiq.io/en/deploy-helm-charts-using-terraform-module
