# terraform.tfvars

- `terraform.tfvars` serves as a way to **store variable values** for your infrastructure configuration. 
- it contains variable names and their corresponding values, separated by an equals sign (`=`).

## why we need `terraform.tfvars`
- **Purpose:** separate variable definitions from Terraform code. This promotes code reusability and makes it easier to manage different environments with different variable values.
- **Benefits:**
    - **Flexibility:** You can easily change variable values by modifying the `terraform.tfvars` file, without altering your Terraform code.
    - **Security:** Sensitive information like API keys or passwords can be kept out of your main Terraform code, potentially enhancing security.
    - **Environment-specific configurations:** You can create multiple `terraform.tfvars` files for different environments (e.g., development, staging, production), each with its own set of variable values.
- **Usage:** Terraform automatically loads variables defined in `terraform.tfvars` when you run commands like `terraform apply`. You can also specify additional `tfvars` files using the `-var-file` flag.

Note that the `terraform.tfvars` file is not **mandatory**. 
We can pass variable values in various ways, such as through command-line flags, environment variables, or interactive prompts.
