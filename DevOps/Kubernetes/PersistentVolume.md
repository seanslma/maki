# Persistent Volume
https://kubernetes.io/docs/concepts/storage/persistent-volumes/

- Volumes cannot mount within other volumes (but see Using subPath for a related mechanism)
- A volume cannot contain a hard link to anything in a different volume

## Volume types
Ephemeral volume types have a lifetime of a pod, but persistent volumes exist beyond the lifetime of a pod. 
 
## Reclaim Policy
https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/#:~:text=PersistentVolumes%20can%20have%20various%20reclaim,user%20deletes%20the%20corresponding%20PersistentVolumeClaim.
- delete
- recycle
- retain
