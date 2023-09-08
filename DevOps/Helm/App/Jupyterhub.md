# Jupyterhub

https://jupyterhub.github.io/helm-chart/

Create a jupyterhub in the kubernetes cluster.

## dedicated node pool for users (taints and tolerations)
https://zero-to-jupyterhub.readthedocs.io/en/latest/administrator/optimization.html

## helm chart setup
https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/HEAD/jupyterhub/values.yaml

## persistent storage
- https://kienmn97.medium.com/persistent-storage-in-jupyterhub-on-kubernetes-cluster-running-on-minikube-4b469bdb1b86
- https://docs.microsoft.com/en-us/azure/aks/azure-files-volume
- https://docs.openshift.com/container-platform/3.10/install_config/persistent_storage/persistent_storage_azure_file
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jhub-storage
  namespace: jhub
spec:
  storageClassName: "standard" # it will be default storage class if unspecified.
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
```

We then need to mount the volume to a path in the hub pod where the database is stored, in `volumes` and `volumeMounts` sections.

## values.yaml
```yaml
  singleuser:
    cpu:
      guarantee: 0.25 #must be number
      limit: 1.5      #must be number
    memory:
      guarantee: 4G
      limit: 16G
```

## failed to list *v1beta1.PodDisruptionBudget: the server could not find the requested resource
https://discourse.jupyter.org/t/readiness-probe-fails-on-docker-kubernetes-deploy/17517/4
```
coming from a newer k8s version and a depreciation of v1beta1
policy/v1beta1 PodDisruptionBudget is deprecated in aks v1.21+, unavailable in aks v1.25+; use policy/v1 PodDisruptionBudget
```
This typically occurs when there's a problem with the Kubernetes `API server` or when the requested resource version is not available or supported.
check the api server status
```
kubectl get componentstatuses
```
