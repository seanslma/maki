# Jupyterhub values.yaml file

## singleuser
```yaml
singleuser:
  uid: 1000
  fsGid: 100
  image:
    name: jupyterhub/k8s-singleuser-sample
    tag: "1.0.0"
    pullPolicy:
    pullSecrets: []
  cpu:
    guarantee: 0.25 #must be number
    limit: 1.5      #must be number
  memory:
    guarantee: 4G
    limit: 16G
  cloudMetadata:
    # block set to true will append a privileged initContainer using the
    # iptables to block the sensitive metadata server at the provided ip.
    blockWithIptables: true
    ip: 169.254.169.254
  extraLabels:
    hub.jupyter.org/network-access-hub: "true"
  storage:
    type: static
    static:
      pvcName: my-pvc
      subPath: "{username}"
    homeMountPath: /home/user
```

## hub
```yaml
hub:
  redirectToServer: false
  allowNamedServers: false
  activeServerLimit: 1
```

### hub.image
```yaml
hub:
  image:
    name: jupyterhub/k8s-hub
    tag: "3.1.1"
    pullPolicy:
    pullSecrets: []
```

### hub.config
```yaml
hub:
  config:
    JupyterHub:
      admin_access: true
      authenticator_class: dummy #azuread
    Authenticator:
      auto_login: true
      admin_users:
        - admin-user-name
```

### hub.db
```yaml
hub:
  db:
    type: sqlite-pvc
```

### hub.extraEnv
Set envvar from kubernetes secret.
- https://z2jh.jupyter.org/en/latest/resources/reference.html#hub-extraenv
- https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/1103
- https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#envvar-v1-core
```yaml
hub:
  extraEnv:
    JHUB_ACCESS_CLIENT_ID
      valueFrom:
        secretKeyRef:
          name: jupyter-user-secret
          key: client_id
    JHUB_ACCESS_CLIENT_SECRET
      valueFrom:
        secretKeyRef:
          name: jupyter-user-secret
          key: client_secret
```

### hub.extraConfig
https://z2jh.jupyter.org/en/latest/resources/reference.html#schema-hub-extraconfig

Arbitrary extra python based configuration that should be in jupyterhub_config.py.
```yaml
hub:
  extraFiles:
    my_config:
      mountPath: /usr/local/etc/jupyterhub/jupyterhub_config.d/my_config.py
      stringData: |
        import os
        c.KubeSpawner.http_timeout = 60
        c.AzureAdOAuthenticator.allow_all = True
        c.AzureAdOAuthenticator.client_secret = os.environ['JHUB_ACCESS_CLIENT_SECRET']
```

### hub.extraFiles
To embed Python code inside a YAML file, consider using `hub.extraFiles` and 
mounting a file to `/usr/local/etc/jupyterhub/jupyterhub_config.d` in order to load your extra configuration logic.
 
The `hub.extraFiles` allows you to inject additional files into the JupyterHub Hub pod. 
These files can be used to customize the look and feel of the Hub, add new features, or provide additional functionality.

Here are some examples of how you can use the hub.extraFiles configuration option:
- Inject custom CSS styling to override the default styling of the Hub.
- Inject custom JavaScript code to add new features or functionality to the Hub.
- Inject configuration files for custom authentication providers or other JupyterHub extensions.
- Inject static files, such as images or fonts, to be used in the Hub's user interface.

## scheduling
```yaml
scheduling:
  userScheduler:
    enabled: false
  userPlaceholder:
    enabled: true
    image:
      name: registry.k8s.io/pause
      tag: "3.9"
  userPods:
    nodeAffinity:
      matchNodePurpose: prefer #require
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

## PrePuller
https://test-zerotojh.readthedocs.io/en/edit-awseks/optimization.html
```yaml
prePuller:
  hook:
    enabled: false
  continuous:
    enabled: false
  pause:
    image:
      name: /registry.k8s.io/pause
      tag: "3.9"
```

Pre-pulling the images on all the nodes can cut this wait time to a few seconds.
- hook: user’s container image is pulled on all nodes whenever a helm install or helm upgrade is performed
- continues: the user’s container image will be pre-pulled when a new node is added
