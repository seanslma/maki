# Job

https://kubernetes.io/docs/concepts/workloads/controllers/job/

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-date
spec:
  schedule: "*/30 * * * *"
  concurrencyPolicy: "Forbid"  
  failedJobsHistoryLimit: 5
  successfulJobsHistoryLimit: 3
  jobTemplate:
    spec:
      backoffLimit: 5
      ttlSecondsAfterFinished: 100
      template:
        spec:
          containers:
          - name: hello-date
            image: my-image
            imagePullPolicy: IfNotPresent
            args:
            - -e
            - "echo date;"
          restartPolicy: OnFailure
      parallelism: 1
      completions: 1
```

## `concurrencyPolicy`
concurrencyPolicy set to Forbid means it will run 0 or 1 times.

## `restartPolicy`
restartPolicy set to Never means it won't restart on failure.

## `.spec.backoffLimit`
The number of `retries` before considering a Job as failed. Default is 6. 

Failed Pods associated with the Job are recreated by the Job controller with an exponential back-off delay (10s, 20s, 40s ...) capped at six minutes. 
The back-off count is reset when a Job's Pod is deleted or successful without any other Pods for the Job failing around that time.

The number of retries is calculated in two ways:
- The number of Pods with `.status.phase = "Failed"`
- When using `restartPolicy = "OnFailure"`, the number of retries in all the containers of Pods with `.status.phase` equal to `Pending` or `Running`
If either of the calculations reaches the .spec.backoffLimit, the Job is considered failed.

When the JobTrackingWithFinalizers feature is disabled, the number of failed Pods is only based on Pods that are still present in the API.
