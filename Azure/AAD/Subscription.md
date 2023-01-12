# Subscription

When a user signs up for a Microsoft cloud service, a new Azure AD tenant is created and the user is made a member of the Global Administrator role.

However, when an owner of a subscription joins their subscription to an existing tenant, the owner isn't assigned to the Global Administrator role.

## change subscription
If resource-group could not be found, change default subscription
```
az login
az login --tenant tenant.onmicrosoft.com
az account list --output table #list all subscriptions
az account set -s <subscription-id>
az account set --subscription <subscription-id> #set default subscription
```

## Role assignment with VS Pro Subscription
https://stackoverflow.com/questions/67486458/how-can-i-associate-a-subscription-with-a-new-tenant-in-azure

Invite a user from new tenant by assigning them a suitable RBAC role in the VS Pro Subscription.
- Subscription
- Access control (IAM)
- Role Assignments
- Add > Owner from the new tenant

### role assignment
https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal

## Associate subscription to another directory
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory

https://vmlabblog.com/2020/02/how-to-move-an-azure-subscription/

## Transfer subscription to another directory
https://docs.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription
