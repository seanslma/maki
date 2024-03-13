# Dependency

## terragrunt `dependency` vs terraform `depends_on`
Scope
- In Terragrunt, we can declare dependencies between modules 
- In Terraform, we can only declare dependencies between resources within a single module

Execution order
- In Terragrunt, dependencies are resolved in a top-down order, where each module is processed before its dependencies
- In Terraform, the depends_on argument is used to specify the execution order of resources within a module
