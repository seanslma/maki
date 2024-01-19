# Group

## group member access to subscription
how to create a security group `az-dev-contributor` in azure aad to let it's members have access to a azure subscription name `az-dev`?

 **Steps on how to create a security group in Azure AD and grant its members access to the "az-dev" subscription:**

**1. Create the Security Group in Azure AD:**

- Sign in to the Azure portal using a user account with sufficient permissions to manage Azure AD groups.
- Go to Azure Active Directory > Groups.
- Click "New group".
- Choose "Security" as the group type.
- Provide a name for the group (e.g., "az-dev-contributor").
- Add a description if desired.
- Select the appropriate membership type (e.g., "Assigned").
- Click "Create".

**2. Assign a Role to the Security Group:**

- Go to Subscriptions > "az-dev" subscription.
- Click on "Access control (IAM)".
- Click "Add" > "Add role assignment".
- Select the appropriate role for the security group (e.g., "Contributor" for general access
  or more specific roles like "Virtual Machine Contributor" or "Storage Blob Data Contributor" as needed).
- Under "Assign access to", click "Select members".
- Search for and select the newly created security group.
- Click "Review + assign".
- Click "Assign".

**3. Add Members to the Security Group:**

- Go back to Azure Active Directory > Groups > "az-dev-contributor" group.
- Click on "Members".
- Click "Add members".
- Search for and select the users or other groups you want to add as members.
- Click "Select".
- Click "Add".

**Key Points:**

- Ensure you have the necessary permissions to create groups and assign roles in Azure AD.
- Choose the appropriate role based on the level of access you want to grant to the group members.
- Consider using more granular roles for specific resource types if needed.
- Regularly review and update group memberships and assigned roles to maintain security and compliance.
- For more complex scenarios or automation, consider using Azure PowerShell or Azure CLI commands.
