# Lock
For resources in production environments that should not be modified or deleted accidentally.

Azure locks can:
- lock resources such that they cannot be deleted, even for owner access
- lock resources such that they can neither be deleted nor have their configuration modified

Locks can be applied at the levels of 
- subscription
- resource group
- management group
- individual resource
