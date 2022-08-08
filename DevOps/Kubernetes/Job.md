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
          - name: print-date
            image: node:14-alpine
            imagePullPolicy: IfNotPresent
            args:
            - -e
            - "console.log(new Date().toString());"
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
