# Node debug

## Check permission
```sh
kubectl auth can-i get namespaces
kubectl auth can-i create namespaces
kubectl auth can-i delete namespaces
```

## Resource capacity
```sh
kubectl resource-capacity -u -p
kubectl get pods -A -o yaml | grep -A5 emptyDir
```

## Check disk usage in node
```sh
# debug into aks node
kubectl debug node/<node-name> -it --image=busybox
# change to node not the pod
chroot /host

df -h

aks node disk usage
after aks version upgrade
Filesystem   Size  Used Avail Use% Mounted on
/dev/root    247G   80G  168G  33% /
before aks version upgrade
Filesystem   Size  Used Avail Use% Mounted on
/dev/root    247G  140G  108G  57% /
```
