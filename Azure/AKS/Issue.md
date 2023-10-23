# Issue

## Unable to connect to the server: dial tcp: lookup : no such host
The `Private Cluster` option is enabled while creating the AKS cluster.
```
az aks show -n <aks-name> -g <resource-group-name> | grep private
```

## Category: ClientError; Code: UpgradeFailed; SubCode: DrainDidNotComplete
https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/error-code-poddrainfailure

Reason: If the `Allowed Disruption` value is 0, the node drain will `fail` during the upgrade process.

Solution:
- Enable pods to drain
- Back up, delete, and redeploy the PDB
```sh
kubectl get pdb <pdb-name> -n <pdb-namespace> -o yaml > pdb_backup.yaml
kubectl delete pdb <pdb-name> -n /<pdb-namespace>
kubectl apply -f pdb_backup.yaml
```  
- Delete the pods that can't be drained
