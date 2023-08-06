# Workflow template

Workflow templates are a library of code that can be reused.

## example
```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: hello
spec:
  entrypoint: main
  templates:
    - name: main
      container:
        image: docker/whalesay
        command: [ cowsay ]
```
