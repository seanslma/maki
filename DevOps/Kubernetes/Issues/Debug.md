# Debug

https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/#create-a-simple-pod-to-use-as-a-test-environment

Sometimes there are network issue we need to solve but the existing pod does not have the diagnostic tools installed.
In this case, we can create a test pod in the same namespace.

## Create a simple Pod to use as a test environment
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dnsutils
  namespace: default
spec:
  containers:
  - name: dnsutils
    image: registry.k8s.io/e2e-test-images/jessie-dnsutils:1.3
    command:
      - sleep
      - "infinity"
    imagePullPolicy: IfNotPresent
  restartPolicy: Always
```

Create the pod and run into it
```sh
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
kubectl get pods dnsutils
kubectl exec -it dnsutils -- bash
```
