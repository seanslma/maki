# Reboot Node

## Get node info
 ```sh
 kubectl get nodes
 kubectl describe node <node-name>
 ```

## Drain the Node (optional but recommended)
Draining a node will safely evict all the pods from the node and schedule them onto other nodes in the cluster. 
This helps to avoid service disruption.

 ```sh
 kubectl drain <node-name> --ignore-daemonsets --delete-local-data
 ```
 - `--ignore-daemonsets`: Skips daemonsets which might be running on the node.
 - `--delete-local-data`: Removes pods with local storage.

If the node is part of a high-availability setup, you may want to wait until the cluster has rescheduled the pods to other nodes before proceeding.

## Restart the Node
On a VM or Physical Server:
```sh
sudo reboot
```

On Cloud Providers:
use the cloud provider's management console or CLI tools to restart the instance
- **Azure:**
 ```bash
 az vm restart --resource-group <resource-group> --name <vm-name>
 ```

- **AWS EC2:**
```bash
aws ec2 reboot-instances --instance-ids <instance-id>
```
- **Google Cloud:**
```bash
gcloud compute instances reset <instance-name> --zone <zone>
```

## Uncordon the Node (if drained)
After the node has restarted, we need to mark it as schedulable again so that new pods can be scheduled onto it.
```bash
kubectl uncordon <node-name>
```

## Verify Node Status
Ensure the node has returned to a Ready state and that it is functioning properly.
- **Check Node Status:**
  ```bash
  kubectl get nodes
  ```
- **Check Node Logs:**
  Depending on your setup, you might want to check system logs or Kubernetes logs to ensure everything is functioning correctly.
