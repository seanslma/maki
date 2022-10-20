# Deployment

## push image to aks
https://learn.microsoft.com/en-us/azure/aks/devops-pipeline?pivots=pipelines-yaml

## clear workspace
https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases?view=azure-devops&tabs=yaml#workspace

Self-hosted agent will not automatically clear all the `workspace` directory
```
  jobs:
  - deployment: MyDeploy
    pool:
      vmImage: 'ubuntu-latest'
    workspace:
      clean: all
    environment: staging
```

May delete needed files, can delete the files manually
```
  - powershell: |
      Remove-Item *.whl
    displayName: Delete whl files
```
