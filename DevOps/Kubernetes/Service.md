# Service

## Internal DNS name
For communicating inside a cluster, the DNS names are like `<service-name>.<namespace>.svc.cluster.local`.
  
## Service Internal Traffic Policy
- enable the internal-only traffic policy for a Service, by setting its `.spec.internalTrafficPolicy` to `Local`
- this tells kube-proxy to only use node local endpoints for cluster internal traffic
```
apiVersion: v1
kind: Service
metadata:
  name: <service-name>
spec:
  ports:
    - port: 8000
  selector:
    app: <app-name>      
  internalTrafficPolicy: Local
```
