# Template
https://killercoda.com/pipekit/course/argo-workflows/templates

## list workflow pods
```sh
kubectl get pods -l workflows.argoproj.io/workflow
```

## Work template
- Container: run a container
- Container Set: run multiple containers in a single pod
- Data: get data from storage 
- Resource: create a Kubernetes resource and wait for it to meet a condition
- Script: run a script in a container

### Container template
```sh
#run
argo submit --watch container-workflow.yaml
#port forward
kubectl -n argo port-forward --address 0.0.0.0 svc/argo-server 2746:2746 > /dev/null &
```
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow                 
metadata:
  generateName: my-container-name 
spec:
  entrypoint: main         
  templates:
  - name: main             
    container:
      image: docker/whalesay
      command: [cowsay]         
      args: ["hello"]
```

## Work orchestration template
- DAG
- Steps
- Suspend
  
### DAG template
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: dag-
spec:
  entrypoint: main
  templates:
    - name: main
      dag:
        tasks:
          - name: a
            template: whalesay
          - name: b
            template: whalesay
            dependencies:
              - a
    - name: whalesay
      container:
        image: docker/whalesay
        command: [ cowsay ]
        args: [ "hello world" ]
```

## Loops
loop over a number of items in parallel using `withItems`
```yaml
dag:
  tasks:
    - name: print-message
      template: whalesay
      arguments:
        parameters:
          - name: message
            value: "{{item}}"
      withItems:
        - "hello"
        - "goodbye"
```

loop over a sequence of numbers using `withSequence`
```yaml
dag:
  tasks:
    - name: print-message
      template: whalesay
      arguments:
        parameters:
          - name: message
            value: "{{item}}"
      withSequence:
        count: 5
```

## Exit Handler
perform a task after something has finished using `Exit Handler` via `OnExit`
```yaml
dag:
  tasks:
    - name: a
      template: whalesay
      onExit: tidy-up
```
