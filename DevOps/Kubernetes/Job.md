# Job

## create job
```
kubectl -n <namespace> create job --from=cronjob/<crojob-name> <job-name> #create a job
kubectl -n <namespace> get job --sort-by=.status.startTime                #show job status
```

## create job from yaml
```
kubectl apply -f <job-name>.yaml
kubectl get jobs -n <namespace>
kubectl delete -f <job-name>.yaml #kubectl delete job <job-name> -n <namespace>
```

## job deployment
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

## suspend cronjob
```
kubectl patch cronjobs <cronjob-name> -p '{"spec" : {"suspend" : true }}'
kubectl patch cronjobs <cronjob-name> -p '{"spec" : {"suspend" : false }}'
```

## `concurrencyPolicy`
- **Allow** (default): allow concurrently running jobs
- **Forbid**: if previous job run hasn't finished yet, the cron job skips the new job run
- **Replace**: if previous job run hasn't finished yet, the cron job replaces the previous running job with a new job run

## `restartPolicy`
- `Never`: it won't restart on failure
- `OnFailure`: the pod will be restarted if it fails
- with `backoffLimit`, a restartPolicy of `Never` ensures that when a pod fails it will eventually propagate and cause the job to fail

## `.spec.backoffLimit`
The number of `retries` before considering a Job as failed. Default is 6. 

Failed Pods associated with the Job are recreated by the Job controller with an exponential back-off delay (10s, 20s, 40s ...) capped at six minutes. 
The back-off count is reset when a Job's Pod is deleted or successful without any other Pods for the Job failing around that time.

The number of retries is calculated in two ways:
- The number of Pods with `.status.phase = "Failed"`
- When using `restartPolicy = "OnFailure"`, the number of retries in all the containers of Pods with `.status.phase` equal to `Pending` or `Running`
If either of the calculations reaches the .spec.backoffLimit, the Job is considered failed.

When the `JobTrackingWithFinalizers` feature is disabled, the number of failed Pods is only based on Pods that are still present in the API.

Note: If the job has restartPolicy = "OnFailure", the Pod running the Job will be terminated once the job backoff limit has been reached. **This can make debugging the Job's executable more difficult**. We suggest setting restartPolicy = "Never" when debugging the Job or using a logging system to ensure output from failed Jobs is not lost inadvertently.

## Degraded job reached the specified backoff limit
The pod will be deleted and this makes it harder to debug the issue. Change the `restartPolicy` to "Never" for debugging.
