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

Only works for aad_pod_identity
```sh
az login --identity      # system-assigned managed identity
az login --identity --username <client_id|object_id|resource_id> # user-assigned managed identity
```

login freeze and timeout issue:
- https://github.com/Azure/azure-cli/issues/12441
- MSI: Failed to acquire tokens after 12 times
- firewall blocked `management.azure.com`

Error:
```
curl -s -H "Metadata: true" "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
Request blocked by AAD Pod Identity NMI
```
Reason: used workload identity but reuires aad_pod_identity

If using workload_identity see the section for workaround
```sh
az login --federated-token "$(cat $AZURE_FEDERATED_TOKEN_FILE)" --service-principal -u $AZURE_CLIENT_ID -t $AZURE_TENANT_ID
```
