# Kube Jobs

https://kubernetes.io/docs/concepts/workloads/controllers/job/

## BackoffLimit
This parameter specifies the number of retries before considering a Job as failed. The back-off limit is set by default to 6. 
Failed Pods associated with the Job are recreated by the Job controller with an exponential back-off delay (10s, 20s, 40s ...) capped at six minutes. 
The back-off count is reset when a Job's Pod is deleted or successful without any other Pods for the Job failing around that time.
