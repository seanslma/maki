# Pod

## General
```
kubectl get pods                #check status
kubectl describe pod <pod-name> #check events
kubectl logs <pod-name>         #check logs
kubectl exec -it <pod-name> -c <container-name> -- bash #connect to pod
```

## ImagePullBackOff
The name of the image might be not correct. Test it:
```
docker pull <repository>/<image>:<tag>
```

## Cronjob pod get killed while executing
https://stackoverflow.com/questions/68643381/why-does-my-kubernetes-cronjob-pod-get-killed-while-executing

The scale down would fail, because it was always preceeded by a scale up, in which point a new node was in the cluster. 

This node had nothing running on it, so the next Job was scheduled on it. 
The Job started on the new node, told Azure to scale down the new node to 0, and subsequently the Kubelet killed the job as it was running.

**Fix**: I changed the spec and added a NodeSelector so that the Job would always run on the system pool, which is more stable than the user pool

