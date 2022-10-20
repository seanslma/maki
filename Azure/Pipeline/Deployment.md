# Deployment

https://learn.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs?view=azure-devops

## checkout repo
A deployment job doesn't automatically `clone the source repo`. You can checkout the source repo within your job with checkout: self. 
Deployment jobs only support one checkout step.
```
- stage: Deploy
  displayName: Deploy Job
  dependsOn: Build
  
  jobs: 
  - deployment: Deploy
    displayName: Build Job Stage  
    environment: Dev
    pool:
      name: my-agent     
    strategy:
      runOnce:
        deploy:
          steps:
            - checkout: self 
```

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
