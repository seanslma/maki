# Kured

KUbernetes REboot Daemon: https://github.com/weaveworks/kured

https://learn.microsoft.com/en-us/azure/aks/node-updates-kured

To protect clusters, security updates are automatically applied to Linux nodes in AKS. Some of these updates require a node reboot to complete the process. 

With kured, a DaemonSet is deployed that runs a pod on each Linux node in the cluster. These pods in the DaemonSet watch for existence of the /var/run/reboot-required file, and then initiate a process to reboot the nodes.
