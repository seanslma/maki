# AdIdentity

## blob storage
https://stackoverflow.com/questions/52769758/azure-blob-storage-authorization-permission-mismatch-error-for-get-request-wit

For blob storage, to let an app to access a specific blob container,
we have to include that blob container in the `azurerm_role_assignment` scope for that app.


