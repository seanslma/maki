# Variable

## Predefined variable
https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml
- Agent.TempDirectory
- Build.SourcesDirectory
- Build.BuildId

## user defined variable
```
variables:
  python_path: 'C:/Python/Python39/'
  artifact_feed: 'my/my_artifact_feed'
  fail_on_no_coverage: true
  dockerRegistryServiceConnection: 'dev'
  imageRepository: my/app'
  dockerfilePath: './docker/Dockerfile'
  tag: '$(Build.BuildId)'
```

# Azure Pipeline Variables
In Azure Pipelines, both **variables** and **parameters** are used to pass and manage values, but they serve different purposes and have different use cases.

## Purpose
Variables are used to store and manage values that you can use throughout your pipeline. 
They can be defined at various scopes and are typically used for storing values that might change during the pipeline execution, such as build numbers, branch names, or environment-specific settings.

## Types
1. **Predefined System Variables**: Provided by Azure Pipelines, such as `Build.BuildId`, `Agent.OS`, and `System.TeamProject`.
2. **User-defined Variables**: Defined by the user in the YAML file or the pipeline UI.

## Scope
- **Pipeline-Level**: Accessible throughout the entire pipeline.
- **Job-Level**: Scoped to a specific job.
- **Step-Level**: Scoped to a specific step.

## Syntax
- **YAML**: `${{ variables['variableName'] }}` or `$(variableName)`
- **Script**: `$VARIABLE_NAME` (when passed as environment variables)

## Example
```yaml
variables:
  buildConfiguration: 'Release'
  myVariable: 'Hello'

steps:
- script: |
    echo $(myVariable)
    echo $(buildConfiguration)
  condition: eq(variables['Agent.OS'], 'windows_nt')
  displayName: 'Print Variables'
```

## Key Characteristics
- Can be overridden by pipeline runs or deployment configurations.
- Can be set in different places: YAML files, the Azure Pipelines UI, or as part of pipeline runs.
- Values can be dynamic and change during runtime.
- Can be used in conditional statements, to set environment variables, or to configure task inputs.
