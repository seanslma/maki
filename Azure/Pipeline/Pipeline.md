# Azure Pipeline
https://levelup.gitconnected.com/up-and-running-with-azure-kubernetes-service-aks-and-devops-pipelines-deployment-40f054071477

https://learn.microsoft.com/en-us/azure/aks/devops-pipeline?pivots=pipelines-yaml

https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/parameters?view=azure-pipelines

AZ-400: Implement CI with Azure Pipelines and GitHub Actions\
https://docs.microsoft.com/learn/paths/az-400-implement-ci-azure-pipelines-github-actions/


https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml

https://azuredevopslabs.com/labs/vstsextend/azurekeyvault/

https://devblogs.microsoft.com/devops/demystifying-service-principals-managed-identities/

## Agent
An agent is an installable software that runs a build or deployment job.

## Artifact
An artifact is a collection of files or packages published by a build. Artifacts are made available for next tasks, such as distribution or deployment.

## Build
A build represents one execution of a pipeline. It collects the logs associated with running the steps and the results of running tests.

### Change pipeline name
- Select pipeline and click e`Edit`
- Click the `vertical ellipse`, in the upper right corner to the right of the Run button
- Select either `Triggers` or `Variables` which will bring up the Visual Designer
- Select the YAML tab
- Specify the new build pipeline name

## Job
A build contains one or more jobs. Most jobs run on an agent.
A job represents an execution boundary of a set of steps. All the steps run together on the same agent.

Types of jobs:
- Agent pool jobs: run on an agent that is part of an agent pool
- Container jobs: run in a container on an agent part of an agent pool
- Deployment group jobs: run on systems in a deployment group
- Agentless jobs: run directly on the Azure DevOps - also often called Server Jobs

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

## Anaconda pipeline
https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/anaconda?view=azure-devops&tabs=ubuntu
