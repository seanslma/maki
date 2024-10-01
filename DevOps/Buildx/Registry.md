# Registry

## push to acr from aks pod
https://github.com/Azure/acr/issues/582
```
error: failed to solve: failed to push my-acr.azurecr.io/dev/test:0.0.1: 
failed to authorize: failed to fetch anonymous token:
unexpected status: 401 Unauthorized
```
bug in buildkit?
- https://github.com/moby/buildkit/blob/ffe2301031c8f8bfb8d5fc5034e5e509c5624913/session/auth/authprovider/authprovider.go#L91
