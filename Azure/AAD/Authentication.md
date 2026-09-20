# Authentication

## Which user is used for authentication

This only works for a user identity (Visual Studio, Azure CLI, VS Code login, etc.)
```py
import requests
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token(
    'https://graph.microsoft.com/.default'
)

resp = requests.get(
    'https://graph.microsoft.com/v1.0/me',
    headers={'Authorization': f'Bearer {token.token}'}
)

print(resp.json())
```
