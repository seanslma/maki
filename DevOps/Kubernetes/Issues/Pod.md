# Pod

## ImagePullBackOff
The name of the image might be not correct. Test it:
```
docker pull <repository>/<image>:<tag>
```

## New pods stuck in Pending without events
If `kube-scheduler` is not running on the master, Kubernetes will report everything as okay but will be unable to start containers in a pod.

Check `kube-scheduler` log
```
kubectl get po -A | grep kube-schedule
kubectl logs <kube-scheduler-name> -n kube-system --tail=20 --timestamps=true
```
if related to certificate and certificate not expire - after renew certs restart master node.

## Cronjob pod get killed while executing
https://stackoverflow.com/questions/68643381/why-does-my-kubernetes-cronjob-pod-get-killed-while-executing

The scale down would fail, because it was always preceeded by a scale up, in which point a new node was in the cluster. 

This node had nothing running on it, so the next Job was scheduled on it. 
The Job started on the new node, told Azure to scale down the new node to 0, and subsequently the Kubelet killed the job as it was running.

**Fix**: I changed the spec and added a NodeSelector so that the Job would always run on the system pool, which is more stable than the user pool

## error determining status: Error response from daemon: readlink /var/lib/docker/overlay2/l/xxxxx: no such file or directory
https://icode.best/i/32712543535032

https://www.cnblogs.com/haoprogrammer/p/11534092.html

Most likely due to disk error, solution (go to the node with issues)
```
# set node to be unschedulable
kubectl cordon <node-name>
kubectl drain <node-name> --ignore-daemonsets

# check file number
cd /var/lib/docker
ls -l overlay2 | wc -l

# clean docker disk
docker system prune --all

# check file number again
ls -l overlay2 | wc -l

# reset node as schedulable
kubectl uncordon <node-name>
```
