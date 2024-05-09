# Middleware

## prefix-removing
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: my-server-stripprefix
  namespace: test
spec:
  stripPrefix:
    prefixes:
      - "/my-prefix"
```
For this middleware, if the path does start with the configured prefix ("/my-prefix"), 
Traefik removes that prefix from the request path before forwarding it to the backend service.

Useful when we have multiple services running behind Traefik, 
- It can simplify backend service configuration by allowing the service to assume a clean path structure regardless of the actual routing prefix used by Traefik.
- It can improve code maintainability if backend code expects a specific URL structure that might be different from the public-facing path.
