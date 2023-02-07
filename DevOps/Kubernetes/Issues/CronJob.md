# CronJob

## `startingDeadlineSeconds`
Error: Cannot determine if job needs to be started: Too many missed start time (> 100). Set or decrease .spec.startingDeadlineSeconds or check clock skew.

https://stackoverflow.com/questions/51065538/what-does-kubernetes-cronjobs-startingdeadlineseconds-exactly-mean/51080214#51080214

- if `startingDeadlineSeconds` = 200, it will count how many missed jobs occurred in the last 200 seconds. 
- if `startingDeadlineSeconds` is not set, the job will be attempted to start by the CronJob controller without checking if it's later or not.

### `CronJob controller`
- The CronJob controller will check the every 10 seconds the list of cronjobs in the given Kubernetes Client.
- For every CronJob, it checks how many schedules it missed in the duration from the lastScheduleTime till now. 
  If there are more than 100 missed schedules, then it doesn't start the job and records the event.
