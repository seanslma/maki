# Azure Pipelines

https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml

https://azuredevopslabs.com/labs/vstsextend/azurekeyvault/

https://devblogs.microsoft.com/devops/demystifying-service-principals-managed-identities/

## Template
https://docs.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops
```
#pipeline-template.yml
parameters:
- name: buildSteps # the name of the parameter is buildSteps
  type: stepList # data type is StepList
  default: [] # default value of buildSteps
stages:
- stage: secure_buildstage
  pool:
    vmImage: windows-latest
  jobs:
  - job: secure_buildjob
    steps:
    - script: echo This happens before code 
      displayName: 'Base: Pre-build'
    - script: echo Building
      displayName: 'Base: Build'
```

```
#azure-pipeline.yml
trigger:
- main

extends:
  template: start.yml
  parameters:
    buildSteps:  
      - bash: echo Test #Passes
        displayName: succeed
      - bash: echo "Test"
        displayName: succeed
      # Step is rejected by raising a YAML syntax error: Unexpected value 'CmdLine@2'
      - task: CmdLine@2
        inputs:
          script: echo "Script Test"
      # Step is rejected by raising a YAML syntax error: Unexpected value 'CmdLine@2'
      - script: echo "Script Test"
```

## Build
### Change pipeline name
- Select pipeline and click edit
- Click the vertical ellipse, in the upper right corner to the right of the Run button
- Select either Triggers or Variables which will bring up the Visual Designer
- Select the YAML tab
- Specify the new build pipeline name

## Azure CLI DevOps Extension
https://adamtheautomator.com/azure-devops/#logging-in-with-the-azure-cli
```
az extension add --name azure-devops
az devops configure --defaults organization=https://<website>

az devops project create --name <project-name>
az devops configure --defaults project=<project-name>
```

## Bash task
https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/bash?view=azure-devops

## build not trigered
Check triggers (maybe overwriten by UI or had connection issues):
```
Edit > three-dots > TRiggers
```

## Anaconda pipeline
https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/anaconda?view=azure-devops&tabs=ubuntu
