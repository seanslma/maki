# System Variables

Azure Pipelines provides a set of predefined system variables that you can use in your pipelines. These variables are automatically populated with information about the pipeline execution environment, agent, build, and more.

## Build Information
- **`Build.BuildId`**: The ID of the build.
- **`Build.BuildNumber`**: The build number.
- **`Build.DefinitionName`**: The name of the build pipeline.
- **`Build.DefinitionId`**: The ID of the build pipeline.
- **`Build.QueuedBy`**: The name of the person who queued the build.
- **`Build.SourceBranch`**: The source branch of the build (e.g., `refs/heads/main`).
- **`Build.SourceBranchName`**: The name of the source branch (e.g., `main`).
- **`Build.SourceVersion`**: The commit ID of the source branch.
- **`Build.Repository.Name`**: The name of the repository.
- **`Build.Repository.Provider`**: The type of repository (e.g., `TfsGit`, `GitHub`).
- **`Build.RequestedFor`**: The name of the person who requested the build.

## Miscellaneous
- **`Build.ArtifactStagingDirectory`**: The directory used to stage build artifacts.
- **`Build.BinariesDirectory`**: The directory where binaries are placed.
- **`Build.SourcesDirectory`**: The directory where source code is downloaded.
- **`Build.Repository.Uri`**: The URL of the repository.

## Agent Information
- **`Agent.OS`**: The operating system of the agent (e.g., `Windows_NT`, `Linux`, `Darwin` for macOS).
- **`Agent.Name`**: The name of the agent.
- **`Agent.MachineName`**: The name of the machine where the agent is running.
- **`Agent.Version`**: The version of the agent.
- **`Agent.ToolsDirectory`**: The directory where tools are installed on the agent.
- **`Agent.TempDirectory`**: The temporary directory used by the agent.
- **`Agent.BuildDirectory`**: The build directory used by the agent.

## Pipeline Information
- **`System.DefinitionId`**: The ID of the pipeline definition.
- **`System.DefinitionName`**: The name of the pipeline definition.
- **`System.TeamProject`**: The name of the project.
- **`System.TeamFoundationCollectionUri`**: The URL of the Azure DevOps organization.
- **`System.TeamFoundationServerUri`**: The URL of the Team Foundation Server (if using TFS).
- **`System.JobId`**: The ID of the job currently running.
- **`System.StageName`**: The name of the current stage in the pipeline.
- **`System.PhaseName`**: The name of the current phase in the pipeline.
- **`System.PreviousSuccessfulBuildId`**: The ID of the previous successful build.
- **`System.PullRequest.PullRequestId`**: The ID of the pull request (for PR builds).

## Release Information
- **`Release.ReleaseId`**: The ID of the release.
- **`Release.ReleaseName`**: The name of the release.
- **`Release.EnvironmentName`**: The name of the release environment.
- **`Release.ReleaseDescription`**: The description of the release.
- **`Release.DefinitionId`**: The ID of the release definition.
- **`Release.DefinitionName`**: The name of the release definition.
