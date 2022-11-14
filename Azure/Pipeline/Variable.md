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
