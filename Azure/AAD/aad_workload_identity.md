# workload identity

## docs
https://azure.github.io/azure-workload-identity/docs/

- user managed identity -> federated credential (new) -> service account (azure_identity)
- service account (azure_identity, azure_identity_binding) -> pod

## Migrate from pod-identity
CLI example:
- https://learn.microsoft.com/en-us/azure/aks/workload-identity-migrate-from-pod-identity
- https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster

Others:
- https://blog.identitydigest.com/migrate-podid/
- https://www.codit.eu/blog/migrating-to-aad-workload-identity-on-azure-kubernetes-service-aks/?country_sel=be
- https://blog.novacare.no/moving-from-aad-pod-identity-to-workload-identity-in-aks/

Very good guide with terraform examples:
- https://cloudchronicles.blog/blog/A-Step-by-Step-Guide-to-installing-Azure-Workload-Identities-on-AKS

## Enable the OIDC Issuer in AKS
https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer
```sh
# create aks with oidc-issuer enabled
az aks create -n my_aks -g my_rg --node-count 1 --generate-ssh-keys --enable-oidc-issuer

# enable oidc-issuer in existing aks
az aks update -n my_aks -g my_rg --enable-oidc-issuer
# show oidc-issuer url
az aks show -n my_aks -g my_rg --query "oidcIssuerProfile.issuerUrl" -o tsv
# rotate oidc key
az aks oidc-issuer rotate-signing-keys -n my_aks -g my_rg
```
We can also include `--enable-workload-identity` without using helm chart to install it separately.

## Install azure workload identity webhook controller
https://www.blakyaks.com/resources/using-azure-workload-identity-on-aks

- This can be done with `--enable-workload-identity` when creating aks. 
- But the helm chart allows customization like namespace, tolerations, etc.
```sh
# install workload-identity-webhook
helm repo add azure-workload-identity https://azure.github.io/azure-workload-identity/charts
helm repo update
helm install workload-identity-webhook azure-workload-identity/workload-identity-webhook \
  --namepace workload-identity-system \
  --create-namespace \
  --set azureTenantID="${AZURE_TENANT_ID}"

# check webhook controller manager
kubectl get po -n workload-identity-system
```

## Federate Service Account
Create `federated_identity_credential` to link between managed identity and service account.
```terraform
resource "azurerm_federated_identity_credential" "main" {
  count               = var.oidc_enabled ? 1 : 0
  name                = "${var.aks_name}-ServiceAccount-${var.aks_namespace}-${var.aks_serviceaccount_name}"
  resource_group_name = var.resource_group_name
  parent_id           = azurerm_user_assigned_identity.main.id
  audience            = var.oidc_audience
  issuer              = var.oidc_issuer_url 
  subject             = "system:serviceaccount:${var.aks_namespace}:${var.aks_serviceaccount_name}"
}
```

```sh
az identity federated-credential create \
    --name ${FEDERATED_IDENTITY_CREDENTIAL_NAME} \    
    --resource-group "${RESOURCE_GROUP}" \
    --identity-name "${USER_ASSIGNED_IDENTITY_NAME}" \
    --issuer "${AKS_OIDC_ISSUER}" \
    --subject system:serviceaccount:"${SERVICE_ACCOUNT_NAMESPACE}":"${SERVICE_ACCOUNT_NAME}" \
    --audience api://AzureADTokenExchange
```

## Replace `AzureIdentity` and `AzureIdentityBinding` by pod `ServiceAccount`
https://blog.novacare.no/moving-from-aad-pod-identity-to-workload-identity-in-aks
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-workload-identity
  namespace: dev
  annotations:
    azure.workload.identity/client-id: 00000000-0000-0000-0000-000000000000  
```
In deployment replace
```yaml
spec:
  template:
    metadata:
      labels:
        app: web
        aadpodidbinding: my-service
```
by
```yaml
spec:
  template:
    metadata:
      labels:
        app: web
        azure.workload.identity/use: "true"
    spec:
      serviceAccountName: my-service-workload-identity
      containers:
      ...
```

In pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod-with-workload-identity
  namespace: ${SERVICE_ACCOUNT_NAMESPACE}
  labels:
    azure.workload.identity/use: "true"  # Required. Only pods with this label can use workload identity.
spec:
  serviceAccountName: ${SERVICE_ACCOUNT_NAME}
  containers:
    - image: <image>
      name: <containerName>
```

## mount key-vault secret as volume
```
Warning  FailedMount  <invalid>  kubelet MountVolume.SetUp failed for volume "config" :
rpc error: code = Unknown desc = failed to mount secrets store objects for pod dev/pod-kv,
err: rpc error: code = Unknown desc = failed to mount objects,
error: failed to get keyvault client: failed to get authorizer for keyvault client:
nmi response failed with status code: 404, response body:
getting assigned identities for pod dev/pod-kv in CREATED state failed after 16 attempts, retry duration [5]s, error: <nil>.
Check MIC pod logs for identity assignment errors
```
This indicates that the pod is still using the `aad_pod_identity` not `workload_identity`.
As this is for using key-vault secret as the mounted volume, in the `SecretProviderClass` we must update
```yaml
cat <<EOF | kubectl apply -f -
# This is a SecretProviderClass example using workload identity to access your key vault
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: azure-kvname-wi # needs to be unique per namespace
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"                # Must be false for workload identity
    clientID: "${USER_ASSIGNED_CLIENT_ID}" # Setting this to use workload identity
    keyvaultName: ${KEYVAULT_NAME}         # Set to the name of your key vault
    cloudName: ""  # [OPTIONAL for Azure] if not provided, the Azure environment defaults to AzurePublicCloud
    objects:  |
      array:
        - |
          objectName: secret1             # Set to the name of your secret
          objectType: secret              # object types: secret, key, or cert
          objectVersion: ""               # [OPTIONAL] object versions, default to latest if empty
        - |
          objectName: key1                # Set to the name of your key
          objectType: key
          objectVersion: ""
    tenantId: "${IDENTITY_TENANT}"        # The tenant ID of the key vault
EOF
```
More detail can be found here: https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-identity-access

## connection to database timed out
checked the version of `azure-identity` which is higher then `1.13.0`.

https://github.com/Azure/azure-workload-identity/issues/976
- Upgrading the package "Microsoft.Data.SqlClient" fixed the issue

https://github.com/Azure/azure-workload-identity/issues/1157
- these links helped me with Python where we now are using ODBC with workload identity

details about workload identity with sql connection
- https://moimhossain.com/2024/03/29/aks-workload-identity-a-deeper-look
- use `token` as well
```py
credential = ClientSecretCredential(tenant_id, client_id, client_secret)    
token_bytes = credential.get_token('https://database.windows.net/.default').token.encode('UTF-16-LE')
token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
SQL_COPT_SS_ACCESS_TOKEN = 1256
conn_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
conn = pyodbc.connect(conn_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})

cursor = conn.cursor()
cursor.execute('SELECT @@version')
```

ODBC driver not supporting AKS workload identity
- https://techcommunity.microsoft.com/t5/azure-database-support-blog/lesson-learned-384-odbc-driver-not-supporting-aks-workload/ba-p/3858209
- workaround (using `token`): https://stackoverflow.com/questions/77134053/login-timeout-expired-while-connecting-to-sql-server-using-workload-identity
```py
import pyodbc, struct   
from azure.identity import DefaultAzureCredential
# Get credentials, default to workload identity
credential = DefaultAzureCredential()
# Get token for Azure SQL Database and convert to UTF-16-LE for SQL Server driver
token_bytes = credential.get_token('https://database.windows.net/.default').token.encode('UTF-16-LE')
token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
# Connect with the token
SQL_COPT_SS_ACCESS_TOKEN = 1256
# can also have `encrypt=yes;trustservercertificate=no;connection timeout=30`
# exclude `authentication=ActiveDirectoryMSI` otherwise will have errors
connString = 'Driver={ODBC Driver 17 for SQL Server};SERVER=dbservere.database.windows.net;DATABASE=db'
conn = pyodbc.connect(connString, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
# Run query
cursor = conn.cursor()
cursor.execute('SELECT @@version')
```

## sqlalchemy for azure sql server 
https://docs.sqlalchemy.org/en/20/dialects/mssql.html#connecting-to-databases-with-access-tokens

Note that the TOKEN_URL` is `https://database.windows.net/.default`, not `https://database.windows.net/`. Otherwise you will get the error `WorkloadIdentityCredential: Microsoft Entra ID error '(invalid_scope) AADSTS70011: The provided request must include a 'scope' input parameter. The provided value for the input parameter 'scope' is not valid. The scope https://database.windows.net/ is not valid.`

If include `Authentication=ActiveDirectoryMsi` will lead to error `Cannot use Access Token with any of the following options: Authentication, Integrated Security, User, Password`.

```py
import struct
from sqlalchemy import create_engine, event
from azure.identity import DefaultAzureCredential

TOKEN_URL = "https://database.windows.net/.default"  # The token URL for any Azure SQL database
SQL_COPT_SS_ACCESS_TOKEN = 1256  # Connection option for access tokens, as defined in msodbcsql.h

connection_string = "mssql+pyodbc://@my-server.database.windows.net/myDb?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string)

@event.listens_for(engine, "do_connect")
def provide_token(dialect, conn_rec, cargs, cparams):
    # remove the "Trusted_Connection" parameter that SQLAlchemy adds
    cargs[0] = cargs[0].replace(";Trusted_Connection=Yes", "")

    # create token credential
    azure_credentials = DefaultAzureCredential()
    raw_token = azure_credentials.get_token(TOKEN_URL).token.encode("utf-16-le")
    token_struct = struct.pack(f"<I{len(raw_token)}s", len(raw_token), raw_token)

    # apply it to keyword arguments
    cparams["attrs_before"] = {SQL_COPT_SS_ACCESS_TOKEN: token_struct}
```
