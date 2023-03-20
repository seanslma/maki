# null_resource

https://faun.pub/terraform-null-provider-and-null-resource-explained-6a8d674cad63

The `null_resource` is commonly used to run scripts on a specified trigger.

Using `local-exec` provider within it means that anything that code actually does, will not be held in the Terraform state file.
