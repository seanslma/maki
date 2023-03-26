# Dependency

## mock outputs
https://terragrunt.gruntwork.io/docs/features/execute-terraform-commands-on-multiple-modules-at-once/

If the module depends on the outputs of another module that hasn't been applied yet, we need to use the `mock_outpus` when `run-all plan/validate`.
