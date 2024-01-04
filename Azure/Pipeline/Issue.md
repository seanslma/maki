# Issue

## build not triggered
Check triggers (maybe overwritten by UI or had connection issues):
```
Edit > three-dots > Triggers
```

## serice connection pat expired
error
```
An error occurred while fetching the YAML file 'azure-pipelines.yml' in the repository's default branch and latest build branches: master.
Error on last attempt: File azure-pipelines.yml not found in repository dev/my-task at version/branch master.
```
solution: check the project service connection and update the pat (from github)
