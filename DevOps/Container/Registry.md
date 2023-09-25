# Registry

## create a private registry for k8s container images
### deployment
https://hub.docker.com/_/registry
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: registry
  namespace: dev
spec:
  replicas: 1
  selector:
    matchLabels:
      app: registry
  template:
    metadata:
      labels:
        app: registry
    spec:
      containers:
        - name: registry
          image: registry:2.8.2
          env:
            - name: REGISTRY_VALIDATION_DISABLED
              value: "true"
            - name: REGISTRY_STORAGE_DELETE_ENABLED
              value: "true"
          ports:
            - containerPort: 5000
          volumeMounts:
            - name: registry-data
              mountPath: /var/lib/registry
      volumes:
        - name: registry-data
          hostPath:
            path: /mnt/dev/container-images 
```
### service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: registry
  namespace: dev
spec:
  ports:
    - name: http
      targetPort: 5000
      port: 5000
  selector:
    app: registry  
```
### ingress
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: registry
  namespace: dev
  annotations:
    kubernetes.io/ingress.class: "traefik"
spec:
  rules:
    - host: docker.example.com
      http:
        paths:
          - path: /
            backend:
              serviceName: registry
              servicePort: http
  tls:
    - secretName: example.com-tls-cert  
```
