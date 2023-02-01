# Agent

Agent can be run as either a service or an interactive process

## Microsoft-hosted agent
- The virtual machine is discarded after pipeline run
- A Microsoft-hosted agent has job time limits
- Can take longer to start your build - Sometimes take several minutes for an agent to be allocated

## Self-hosted agent
https://github.com/Microsoft/azure-pipelines-agent/releases
- Set up and manage on your own
- Might need to clear the env after each run
- A self-hosted agent doesn't have job time limits
- Can run incremental builds - doesn't clean the repo or do a clean build so the builds will typically run faster

## Personal access token (PAT)
The pat will be used when run `config.sh` in agent folder:
- PAT is the only scheme that works with Azure Pipelines
- PAT is used only when registering the agent and not for succeeding communication
- Create a PAT: User settings > Security > Personal access tokens > New Token
- scope: Agent Pools (read & manage); Deployment group (read & manage)

Check pat expiration:
https://gist.github.com/ydkn/e4ee3da80b2d9f8714faa395c9c554ed

## Manage agent pools
https://microsoftlearning.github.io/AZ400-DesigningandImplementingMicrosoftDevOpsSolutions/Instructions/Labs/AZ400_M03_L04_Configuring_Agent_Pools_and_Understanding_Pipeline_Styles.html

## Self-hosted Linux agents
https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux?view=azure-devops
- Settings: {Name: Agent name, Scope (custom defined): Agent Pools, Permissions: read and manage}
- Config: Azure DevOps > Organization settings > Pipelines: Agent pools > Add pool {Self-hosted}
- Agent pools > Jobs > New Agent > download and run config.sh to config agent
- Server-url: https://dev.azure.com/{your-organization}
- Run agent: ./run.sh --once; As a service: sudo ./svc.sh install/start/status/stop/uninstall
- Remove agent: ./config.sh remove



