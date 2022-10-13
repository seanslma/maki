# Azure

## Active directory I am in
```
$user = "my.name@example.com"
Connect-AzureAD
Get-AzureADUserMembership -ObjectId $user | Select DisplayName, ObjectId
```
