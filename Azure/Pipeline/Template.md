# Template
https://docs.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops

## order
script(bash, task etc.) must in the first line. generally in this order:
- script
- displayName
- inputs
- condition

## template file
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

## pipeline file
```
#azure-pipeline.yml
trigger:
  - master
  - refs/tags/*
pr:
  - master
pool:
  vmImage: 'linux-latest'
variables:
  var1: v1
resources:
  repositories:
    - repository: templates
      type: github
      name: <namespace>/<pipeline-template>
      endpoint: unknown
      ref: refs/heads/<branch-name>
jobs:
  - template: jobs/pipeline-template.yml@templates
    parameters:
      test: True
```
