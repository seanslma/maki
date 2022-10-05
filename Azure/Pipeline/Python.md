# Python

https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python?view=azure-devops

https://medium.com/@anthonypjshaw/azure-pipelines-with-python-by-example-aa65f4070634

## Use Python Version
https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/tool/use-python-version?view=azure-devops&viewFallbackFrom=vsts
```
- task: UsePythonVersion@0
  displayName: Use python version
  inputs:
    versionSpec: '3.9'  #python version
    addToPath: true     #prepend the retrieved Python version to the PATH environment variable
    architecture: 'x64' #options: x86 (windows only), x64 (this argument applies only on windows agents)
```

## Package: Python Pip Authenticate
Must run before use pip to download python distributions to an authenticated package source such as Azure Artifacts.

https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/package/pip-authenticate?view=azure-devops
```
- task: PipAuthenticate@1
  displayName: Pip artifact feeds authenticate
  inputs:
    artifactFeeds: 'proj1/myFeed1, myFeed2' #list of feed names, can use ${{ variables.artifact_feed }}

# Use command line tool to 'pip install'
- script: |
    pip install myPackage
```

## Publish Build Artifacts
Publish build artifacts to Azure Pipelines, TFS, or a file share.

https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/publish-build-artifacts?view=azure-devops
```
- task: PublishBuildArtifacts@1
displayName: Publish build artifacts
inputs:
    pathToPublish: $(Agent.TempDirectory)/pkg
    artifactName: pkg
```

## Download Pipeline Artifacts
Download pipeline artifacts from earlier stages in this pipeline, or from another pipeline.

https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/download-pipeline-artifact?view=azure-devops
```
- task: DownloadPipelineArtifact@2
  displayName: Download pipeline artifacts
  inputs:
    artifact: 'pkg'
    path: $(Build.SourcesDirectory)
```

## Docker
Build and push Docker images to any container registry by using a Docker registry service connection.

https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/build/docker?view=azure-devops&tabs=yaml
```
- task: Docker@2
  displayName: Login to ACR
  inputs:
    command: login
    containerRegistry: dockerRegistryServiceConnection1
- task: Docker@2
  displayName: Login to Docker Hub
  inputs:
    command: login
    containerRegistry: dockerRegistryServiceConnection2
- task: Docker@2
  displayName: Build a Docker image
  inputs:
    command: build
    repository: $(imageRepository)
    containerRegistry: $(dockerRegistryServiceConnection)
    dockerfile: $(dockerfilePath)
    arguments: '--platform linux/amd64'
    tags: |
        $(tag)
        latest
- task: Docker@2
  displayName: Push an image to container registry
  inputs:
    command: push
    repository: $(imageRepository)
    containerRegistry: $(dockerRegistryServiceConnection)
    tags: |
        $(tag)
        latest
```
