# Account

## update password
```sh
az login --scope https://management.azure.com//.default
az login --scope https://management.core.windows.net//.default
```

## Error: Credential authentication unavailable
Run the command first:
```sh
az account list -o table
az account set --subscription <subscription-id>
az login
```

## Continuous access evaluation resulted in challenge with result
- `InteractionRequired and code: TokenCreatedWithOutdatedPolicies`
- `InteractionRequired and code: TokenIssuedBeforeRevocationTimestamp`

Solution:
```sh
az logout
az login
```

## login using managed identity
https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli-managed-identity
```sh
az login --identity      # system-assigned managed identity
az login --identity --username <client_id|object_id|resource_id> # user-assigned managed identity
```

login freeze and timeout issue:
- https://github.com/Azure/azure-cli/issues/12441
- firewall blocked `management.azure.com`

