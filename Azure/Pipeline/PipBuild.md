# Pip build

```
variables:
  docker_file: './docker/linux/repo.docker'
  artifact_feed: 'my/artifact_feed'
  docker_reg_service_conn: 'docker_registry_service_connection'
  docker_image_repository: 'my/app'
  conda_env: 'env'
  tag: '$(Build.BuildId)'

trigger:
- main

resources:
- repo: self

stages:
- stage: Build
  displayName: Build package stage
  jobs:
  - job:
    displayName: Build pip whl
    pool:
      vmImage: 'ubuntu-latest'
    steps:

    - task: UsePythonVersion@0
      displayName: Use python version
      inputs:
        versionSpec: '3.9'
        addToPath: true
        architecture: 'x64'

    - task: PipAuthenticate@0
      displayName: Configure artifact feed authentication
      inputs:
        artifactFeeds: ${{ variables.artifact_feed }}

    - bash: |
        printenv
      displayName: Print environment variables

    - bash: |
        python -m venv $(Agent.TempDirectory)/venv
        source $(Agent.TempDirectory)/venv/bin/activate
        python -m pip install --upgrade pip twine
      displayName: Create virtual environment

    - bash: |
        source $(Agent.TempDirectory)/venv/bin/activate
        pip wheel $(Build.SourcesDirectory) --no-deps -w $(Agent.TempDirectory)/pkg --no-cache-dir --verbose
      displayName: Build wheel file
      # Run from within tmp_dir - setuptools places build files in cur_dir and does not remove them after build
      workingDirectory: $(Agent.TempDirectory)

    - bash: |
        source $(Agent.TempDirectory)/venv/bin/activate
        pip install `cd  $(Agent.TempDirectory)/pkg/ && realpath *`[test] --no-cache-dir --verbose
      displayName: Install built package

    - task: PublishBuildArtifacts@1
      displayName: Publish artifacts
      inputs:
        pathToPublish: $(Agent.TempDirectory)/pkg
        artifactName: pkg

- stage: BuildDocker
  displayName: Build docker image stage
  jobs:
  - job:
    displayName: Build python docker image
    pool:
      name: linux-dev
    steps:

    - task: DownloadPipelineArtifact@2
      displayName: Download pipeline artifacts
      inputs:
        artifact: 'pkg'
        path: $(Build.SourcesDirectory)

    - task: Docker@2
      displayName: Build docker image
      inputs:
        command: build
        repository: $(docker_image_repository)
        containerRegistry: $(docker_reg_service_conn)
        dockerfile: $(docker_file)
        arguments: '--platform linux/amd64 --build-arg NAME=${{ variables.conda_env }}'
        buildContext: .
        tags: |
          $(tag)
          latest

    - task: Docker@2
      displayName: Push docker image to container registry
      inputs:
        command: push
        repository: $(docker_image_repository)
        containerRegistry: $(docker_reg_service_conn)
        tags: |
          $(tag)
          latest
```
