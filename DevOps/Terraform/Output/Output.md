# Output

## show output values
After running `terrafrom apply`, we can use `terrafrom output` to show the values defined in outputs.

## export the state
```sh
terraform state pull > module_test_state.tfstate
```
