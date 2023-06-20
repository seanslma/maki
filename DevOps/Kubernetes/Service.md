# Service

## Internal DNS name
For communicating inside a cluster, the DNS names are like `<service-name>.<namespace>.svc.cluster.local`.

## Service Internal Traffic Policy
- enable the internal-only traffic policy for a Service, by setting its `.spec.internalTrafficPolicy` to `Local`
- this tells kube-proxy to only use node local endpoints for cluster internal traffic

```yaml
apiVersion: v1
kind: Service
metadata:
  name: <service-name>
  namespace: <namespace>
spec:
  ports:
    - port: 8000
  selector:
    app: <app-name>
  internalTrafficPolicy: Local
```

## NodePort
A NodePort is a type of service that allows you to expose your application outside of the cluster by assigning a static port on each cluster node. It's one of the ways to make your application accessible from outside the Kubernetes cluster.

- The assigned `NodePort` should be open in the firewall rules of your cluster's network configuration to allow incoming traffic.
- We can access the application using any node's IP address and the assigned NodePort, such as `http://192.168.0.100:30007`
- default HTTP port (port 80)
- default HTTPS port (port 443)
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
