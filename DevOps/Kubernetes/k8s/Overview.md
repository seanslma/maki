# Overview

- A `Kubernetes cluster` consists of a set of worker machines, called nodes, that run containerized applications.
- The `worker node`(s) host the Pods that are the components of the application workload.
- The `control plane` manages the worker nodes and the Pods in the cluster.

## Control Plane Components
- `etcd`: Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.
- `kube-apiserver`:  API server is the front end for the Kubernetes control plane.
- `kube-scheduler`: Watche for newly created Pods with no assigned node, and selects a node for them to run on.
- `kube-controller-manager`: Node, Job, EndpointSlice, ServiceAccount controllers.
- `cloud-controller-manager`: Link cluster into cloud provider's API,
   and separate out the components that interact with that cloud platform from components that only interact with your cluster.

## Node Components
- `kubelet`: Make sure that containers are running in a Pod.
- `kube-proxy`: Maintain network rules on nodes.
- `Container runtime`: Responsible for running containers.
