# API

## no kind "KubeSchedulerConfiguration" is registered for version "kubescheduler.config.k8s.io/v1"
no kind "KubeSchedulerConfiguration" is registered for version "kubescheduler.config.k8s.io/v1" in scheme "k8s.io/kubernetes/pkg/scheduler/apis/config/scheme/scheme.go:30"

Possible reasons:
- not use the correct version of the KubeSchedulerConfiguration API.
  Check the cluster supported KubeSchedulerConfiguration API: `kubectl get apiservices -o jsonpath='{.items[?(@.metadata.name=="kubescheduler.config.k8s.io")].apiVersion}'`
- the custom KubeSchedulerConfiguration file is not registered with the Kubernetes scheduler.
  To register a custom KubeSchedulerConfiguration file called `kube-scheduler.yaml`: `kube-scheduler --config=kube-scheduler.yaml`

If the command does not show any supported API, most likely
- using an older version of Kubernetes that does not include the KubeSchedulerConfiguration API.
- deleted the KubeSchedulerConfiguration API from your Kubernetes cluster.
- there is a problem with your Kubernetes cluster configuration.
Trouble shooting
- Check the version of Kubernetes `kubectl version`
- Check the Kubernetes cluster configuration `kubectl config view`
  Look for the `kubescheduler.config.k8s.io` API in the apiservices section. If the API is not listed, you will need to add it.
- Restart the Kubernetes scheduler service `kubectl rollout restart deployment kube-scheduler -n kube-system`
