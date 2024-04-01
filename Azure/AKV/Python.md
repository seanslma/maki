# Python

## import
```py
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import (    
    ServiceRequestError,
    ResourceNotFoundError,
)
```

## get keyvault secret
https://stackoverflow.com/questions/64613699/how-to-add-azure-python-sdk-exceptions-to-try-except-statements
```py
def get_keyvault_secret(
    vault_url: str,
    secret_name: str,
) -> dict:
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    data = None
    try:
        secret = client.get_secret(secret_name)
        data = json.loads(secret.value)
    except ServiceRequestError:
        msg = f'Error connecting to Azure Key Vault: {vault_url}'
        warnings.warn(msg, RuntimeWarning)
    except ResourceNotFoundError:
        msg = (
            f'Secret name `{secret_name}` not '
            f'found in Azure Key Vault `{vault_url}`'
        )
        warnings.warn(msg, RuntimeWarning) 
    return data
```
