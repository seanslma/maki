# Node

## 0/x nodes are available y node(s) were unschedulable
Node might have issues:
- `Taint: node.kubernetes.io/unschedulable:NoSchedule`
- `Unschedulable:true`
```
kubectl get nodes #check status
kubectl describe node <node-name> #check details
```
