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
