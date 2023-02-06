# Node

## 0/x nodes are available y node(s) were unschedulable
Node might have issues:
- `Taint: node.kubernetes.io/unschedulable:NoSchedule`
- `Unschedulable:true`
```
kubectl get nodes #check status
kubectl describe node <node-name> #check details
```

## state not ready
https://www.containiq.com/post/debugging-kubernetes-nodes-in-not-ready-state
```
kubectl get pods -n kube-system -o wide
kubectl describe pod <pod-name> -n kube-system
kubectl logs <pod-name> -n kube-system
kubectl describe daemonset kube-proxy -n kube-system

kubectl describe node nodeName
```
