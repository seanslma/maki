# Agent

- agent can be run as either a service or an interactive process

## Microsoft-hosted agent
- The virtual machine is discarded after pipeline run
- A Microsoft-hosted agent has job time limits
- Can take longer to start your build - Sometimes take several minutes for an agent to be allocated

## Self-hosted agent
- Set up and manage on your own
- Might need to clear the env after each run
- A self-hosted agent doesn't have job time limits
- Can run incremental builds - doesn't clean the repo or do a clean build so the builds will typically run faster

## Personal access token (PAT)
- PAT is the only scheme that works with Azure Pipelines
- PAT is used only when registering the agent and not for succeeding communication