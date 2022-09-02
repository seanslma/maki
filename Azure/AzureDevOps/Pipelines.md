# Azure Pipelines

https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml

https://azuredevopslabs.com/labs/vstsextend/azurekeyvault/

https://devblogs.microsoft.com/devops/demystifying-service-principals-managed-identities/

## Template
https://docs.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops
```
#pipeline-template.yml
parameters:
- name: test
  type: bool
  default: False
variables:
- name: check
  value: ok   
stages:
- stage: buildstage
  pool:
    vmImage: windows-latest
  jobs:
  - job: buildjob
    steps:
    - script: echo Building
      displayName: 'Base: Build'
      condition: and(succeeded(), or(eq(variables['check'], 'ok'), eq('${{ parameters.test }}', True)))
```

```
#azure-pipeline.yml
variables:
  var1: v1
trigger:
  - master
  - refs/tags/*
pr:
  - master
resources:
  repositories:
    - repository: templates
      type: github
      name: <namespace>/<pipeline-template>
      endpoint: unkonwn
      ref: refs/heads/v4
jobs:
  - template: jobs/pipeline-template.yml@templates
    parameters:
      test: True
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
