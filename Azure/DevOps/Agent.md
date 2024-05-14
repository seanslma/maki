# Agent
https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser

## self-hosted agent
https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/docker?view=azure-devops#linux
env vars:
- `AZP_URL`: The URL of the Azure DevOps or Azure DevOps Server instance
- `AZP_TOKEN`: Personal Access Token (PAT) with Agent Pools (read, manage) scope, created at AZP_URL
- `AZP_AGENT_NAME`: Agent name (default value: the container hostname)
- `AZP_POOL`: Agent pool name (default value: Default)
- `AZP_WORK`: Work directory (default value: _work)

## aks self-hosted agent
https://medium.com/@muppedaanvesh/azure-devops-self-hosted-agents-on-kubernetes-part-1-aa91e7912f79

https://ghoshasish99.medium.com/azure-devops-self-hosted-agents-on-kubernetes-51685fde9a14

docker build:
- deregister the agent

## How to add a build agent with Azure Container Instances
https://www.vivienfabing.com/azure-devops/2019/06/20/azure-pipelines-how-to-add-a-build-agent-with-azure-container-instances-part-2-custom-agent.html

## azure scale-set agent
https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/scale-set-agents?view=azure-devops
