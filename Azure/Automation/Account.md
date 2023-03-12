# Account

https://blog.johnfolberth.com/deploying-azure-automation-account-and-runbooks-via-terraform/

- In Azure Automation no components talk to each other directly
- Automation account is managed by a management service
- The management service is a single point of contact for all activities within Azure Automation
- All requests from the portal are sent to the automation management service

## Run As account
- Azure Automation accounts do not have access to any resources by default
- Run As account is one way to provide access to subscriptions and the resources
