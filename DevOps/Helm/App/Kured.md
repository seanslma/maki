# Kured

KUbernetes REboot Daemon: https://github.com/weaveworks/kured

https://learn.microsoft.com/en-us/azure/aks/node-updates-kured

To protect clusters, security updates are automatically applied to Linux nodes in AKS. Some of these updates require a node reboot to complete the process. 

With kured, a DaemonSet is deployed that runs a pod on each Linux node in the cluster. These pods in the DaemonSet watch for existence of the /var/run/reboot-required file, and then initiate a process to reboot the nodes.

## cli
```
helm install kured stable/kured --namespace kured --set extraArgs.reboot-days="Mon\,Tue"
```

## check logs
```
kubectl -n <namespace> logs <kured-pod-name>
```
Result
```
"Reboot schedule: SunMonTueWedThuFriSat between 00:00 and 23:59 UTC"
```

## reboot schedule
- `--start-time`: string, schedule reboot only after this time of day (default "0:00")
- `--end-time`: string, schedule reboot only before this time of day (default "23:59:59")
- `--reboot-days`: strings, schedule reboot on these days (default [su,mo,tu,we,th,fr,sa]
```
--reboot-days=mon,tue,wed,thu,fri
--start-time=9am
--end-time=5pm
--time-zone=America/Los_Angeles
```
Times can be formatted in numerous ways, including `5pm`, `5:00pm`, `17:00`, and `17`.

## configuration
https://kured.dev/docs/configuration/

In values.yaml
```
extraArgs:
  start-time: "0:00"
  end-time: "23:59"
  reboot-days: "Mon,Tue"
```
becomes
```
/usr/bin/kured ... --start-time="0:00" --end_time="23:59" --reboot-days="Mon\,Tue"
```

## error: DaemonSet.apps "kured" is invalid: spec.selector: ... field is immutable
https://github.com/kubereboot/kured/issues/610

Solution:
uninstall the release and install it again - cannot simply upgrade
