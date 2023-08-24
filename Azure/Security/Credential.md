# Credential

## This request is not authorized to perform this operation using this permission
- The Azure Blob stoarge path might not be correct.

## Check which credential is used by python
```py
import sys
import logging
from azure.identity import DefaultAzureCredential

logger = logging.getLogger('azure.identity')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('[%(levelname)s] %(name)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

credential = DefaultAzureCredential()
```

If the message is like
```
[INFO] azure.identity.aio._credentials.environment: No environment configuration found.
[INFO] azure.identity.aio._credentials.managed_identity: ManagedIdentityCredential will use IMDS
```
but still crashed in jupyter notebook when get files from Azure Blob Storage via `adlfs`
```
ClientAuthenticationError: DefaultAzureCredential failed to retrieve a token from the included credentials.
Attempted credentials:
	EnvironmentCredential: EnvironmentCredential authentication unavailable. Environment variables are not fully configured.
	ManagedIdentityCredential: ManagedIdentityCredential authentication unavailable, no response from the IMDS endpoint.
	SharedTokenCacheCredential: SharedTokenCacheCredential authentication unavailable. No accounts were found in the cache.
	AzureCliCredential: Azure CLI not found on path
	AzurePowerShellCredential: Failed to invoke PowerShell.
```
Restart `jupyter lab` server. 

## Azure ChainedTokenCredential Fails after Password Change
```
SharedTokenCacheCredential: Azure Active Directory error '(invalid_grant) AADSTS50173: 
The provided grant has expired due to it being revoked, a fresh auth token is needed. 
The user might have changed or reset their password.
```

Solution 1, delete the cache the credential uses. 
When solution 3 does not work try this one.
```
%LOCALAPPDATA%\.IdentityService\msal.cache
```

Solution 2, 
```
credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
```

Solution 3, Clear Azure credential cache using az cli or powershell
use az cli
```sh
az account clear
```
use powershell
- Install `Az-Cmdlets` for powershell
- Run `Clear-AzContext` to clear cached credentials in powershell

## Add credentials via client app's registration
Let container access the azure blob storage via `EnvironmentCredential`:
https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential?view=azure-dotnet

https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-credentials-to-your-web-application
