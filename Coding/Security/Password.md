# Password

## password best practices
https://learn.microsoft.com/en-us/aspnet/identity/overview/features-api/best-practices-for-deploying-passwords-and-other-sensitive-data-to-aspnet-and-azure
- you should never store passwords or other sensitive data in source code
- you shouldn't use production secrets in development and test mode
- usie a "secrets manager" service, such as Azure Key Vault, AWS Secrets Manager

## azure key-vault 
```cs
var keyVaultUrl = "https://<your-key-vault-name>.vault.azure.net/";
var credential =  new DefaultAzureCredential();    
var client = new SecretClient(vaultUri: new Uri(keyVaultUrl), credential);    
KeyVaultSecret secret = client.GetSecret("<your-secret-name>");    
Console.WriteLine($"{secret.Name}: {secret.Value}");
```

## aws secret manager
```cs
var client = new AmazonSecretsManagerClient(
    accessKeyId, secretAccessKey, 
    RegionEndpoint.APSoutheast2
);
var request = new GetSecretValueRequest {
    SecretId = secretName
};
GetSecretValueResponse response = null;
response = client.GetSecretValueAsync(request).Result;
```
