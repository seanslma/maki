# Subscription

## change subscription
If resource-group could not be found, change default subscription
```
az login
az login --tenant tenant.onmicrosoft.com
az account list --output table #list all subscriptions
az account set --subscription <subscription-id> #set default subscription
```

## Role assignment with VS Pro Subscription
https://stackoverflow.com/questions/67486458/how-can-i-associate-a-subscription-with-a-new-tenant-in-azure

Invite a user from new tenant by assigning them a suitable RBAC role in the VS Pro Subscription.
- Subscrition
- Access control (IAM)
- Role Assignments
- Add > Owner from the new tenant

## Associate subscription to another directory
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory

## Transfer subscription to another directory
https://docs.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription
