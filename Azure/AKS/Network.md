# Network

## outbound connections
https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/basic-troubleshooting-outbound-connections

Tools:
- `kubectl` connect to the cluster
- `apt-get` handle packages
- `curl`
- `host` DNS lookups
- Netcat (nc) TCP connections
- `traceroute` print the trace of routing packets to the network host

## Check DNS resolution
If we cannot install the tools, we have to create a pod with the tools already being installed: 
https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/#create-a-simple-pod-to-use-as-a-test-environment
```sh
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
```

create a test pod and install test packages 
```sh
kubectl run -it --rm aks-ssh --namespace <namespace> --image=debian:stable
apt-get update -y
apt-get install dnsutils -y
apt-get install curl -y
apt-get install netcat -y
```

## Check if cluster can reach the endpoint
```sh
kubectl run -it --rm aks-ssh --namespace <namespace> --image=debian:stable
apt-get update -y
apt-get install traceroute -y
apt-get install netcat -y

# Check the route to the endpoint 
traceroute -T microsoft.com -m 50 -p 443

# Check whether the desired port is open on the remote host
nc -z -v microsoft.com 443

# Check the HTTP response code
curl -Iv https://microsoft.com

# Check whether we can connect to any other endpoint
curl -Iv https://kubernetes.io
```
