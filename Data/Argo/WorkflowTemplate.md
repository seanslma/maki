# Workflow template

## workflow template
A workflow template is a library of code that can be reused.
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

## cron workflow
A cron workflow runs on a schedule.
```yaml
apiVersion: argoproj.io/v1alpha1
kind: CronWorkflow
metadata:
  name: cron
spec:
  schedule: "* * * * *"
  workflowSpec:
    entrypoint: main
    templates:
      - name: main
        container:
          image: docker/whalesay
```
