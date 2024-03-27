# Authorization
- https://learn.microsoft.com/en-us/entra/identity-platform/index-web-app?pivots=devlang-python&tabs=windows
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
- https://intility.github.io/fastapi-azure-auth/usage-and-faq/calling_your_apis_from_python/

If someone wants to use your API, they should create their own app registration and their own secret.

## get token
```py
azure_resp = client.post(
    url=f'https://login.microsoftonline.com/{settings.TENANT_ID}/oauth2/v2.0/token',
    data={
        'grant_type': 'client_credentials',
        'client_id': settings.CLIENT_ID,  # app reg (client) id
        'client_secret': settings.CLIENT_SECRET,  # secret created in app reg
        'scope': f'api://{settings.APP_CLIENT_ID}/.default',  # note: NOT .user_impersonation
    }
)
token = azure_resp.json()['access_token']
```

## call api with token
```py
api_resp = client.get(
    'http://localhost:8000/api/hello',
    headers={'Authorization': f'Bearer {token}'},
)
print(api_resp.json())
```
