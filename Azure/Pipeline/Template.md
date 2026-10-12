# Template
https://docs.microsoft.com/en-us/azure/devops/pipelines/process/templates?view=azure-devops

## azure pipeline templates
- create validation pipeline so each change in the templates repo will be tested by itself
- create a tests folder with different test scenarios: build conda, unit test, build docker image etc.
- scripts must be copied and in the right folder, otherwise it cannot be found
- sometimes variables can be used to replace scripts

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
