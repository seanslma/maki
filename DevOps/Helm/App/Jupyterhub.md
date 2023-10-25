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

### userScheduler 
If you have users starting new servers while the total number of active users is decreasing, how will you free up a node so it can be scaled down?
`user scheduler` will schedule new user pods to the most utilised node.

Only activate the user scheduler if you have an `autoscaling` node pool.

### userPlaceholder
The UserPlaceholders is a powerful feature that can improve the performance and scalability of JupyterHub.

The purpose of userPlaceholder in JupyterHub is to pre-allocate resources for users before they need them. This can improve the startup time of Jupyter sessions and reduce the load on the Kubernetes cluster.

UserPlaceholders are small, lightweight pods that are deployed to the Kubernetes cluster. They are configured to consume the same resources as a typical Jupyter session. When a user requests a Jupyter session, JupyterHub will schedule the session on a userPlaceholder pod. This allows the Jupyter session to start immediately, without having to wait for a new pod to be deployed.

UserPlaceholders are also useful for scaling JupyterHub. When the cluster is idle, JupyterHub can scale down the number of userPlaceholder pods. This saves resources and reduces costs. When new users request Jupyter sessions, JupyterHub can quickly scale up the number of userPlaceholder pods to meet the demand.

Here are some of the benefits of using userPlaceholders in JupyterHub:
- **Reduced startup time:** Jupyter sessions can start immediately, without having to wait for a new pod to be deployed.
- **Reduced load on the Kubernetes cluster:** UserPlaceholders are small and lightweight pods, so they do not consume as many resources as a typical Jupyter session.
- **Improved scalability:** JupyterHub can quickly scale up or down the number of userPlaceholder pods to meet the demand.

### PrePuller
https://test-zerotojh.readthedocs.io/en/edit-awseks/optimization.html

Pre-pulling the images on all the nodes can cut this wait time to a few seconds.
- hook: user’s container image is pulled on all nodes whenever a helm install or helm upgrade is performed
- continues: the user’s container image will be pre-pulled when a new node is added

## failed to list *v1beta1.PodDisruptionBudget: the server could not find the requested resource
https://discourse.jupyter.org/t/readiness-probe-fails-on-docker-kubernetes-deploy/17517/4
```
coming from a newer k8s version and a depreciation of v1beta1
policy/v1beta1 PodDisruptionBudget is deprecated in aks v1.21+, unavailable in aks v1.25+; use policy/v1 PodDisruptionBudget
```
This typically occurs when there's a problem with the Kubernetes `API server` or when the requested resource version is not available or supported.
check the api server status
```sh
kubectl get componentstatuses
```

## spawn timeout and solution
https://blog.51cto.com/u_15946369/6035967

## hook-iamge-puller ImagePullBackOff
```
connection reset by peer
```
https://www.modb.pro/db/179200

