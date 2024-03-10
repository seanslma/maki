# DNS

https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/troubleshoot-dns-failure-from-pod-but-not-from-worker-node

## How it works
For DNS resolution, the pods send requests to the `CoreDNS` pods in the kube-system namespace
- If the DNS query is for an internal component, such as a service name, the `CoreDNS` pod responds by itself 
- If the request is for an external domain, the CoreDNS pod sends the request to the `upstream DNS server`

The `upstream DNS servers` are obtained based on the `resolv.conf` file of the worker node in which the pod is running. 
The resolv.conf file (/run/systemd/resolve/resolv.conf) is updated based on the DNS settings of the virtual network on which the worker node is running.

## debug DNS
https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/

First create a test pod in the same namespace
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dnsutils
  namespace: <namespace>
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

Then run commands
```sh
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
kubectl get pods dnsutils
kubectl exec -it dnsutils -- nslookup kubernetes.default
kubectl exec -it dnsutils -- cat /etc/resolv.conf
```
