# Account

https://blog.johnfolberth.com/deploying-azure-automation-account-and-runbooks-via-terraform/

- In Azure Automation no components talk to each other directly
- Automation account is managed by a management service
- The management service is a single point of contact for all activities within Azure Automation
- All requests from the portal are sent to the automation management service
