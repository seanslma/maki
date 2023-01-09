# Terragrunt

https://repo1.dso.mil/platform-one/big-bang/customers/template/-/tree/main/terraform

https://terragrunt.gruntwork.io/docs/reference/config-blocks-and-attributes/

- make providers dry
- make backend dry
- will automatically determine dependencies

## install in linux from binary
find the latest in the assets section in: https://github.com/gruntwork-io/terragrunt/releases
```
wget https://github.com/gruntwork-io/terragrunt/releases/download/v0.42.5/terragrunt_linux_amd64
mv terragrunt_linux_amd64 terragrunt
chmod u+x terragrunt
sudo mv terragrunt /usr/local/bin/terragrunt
terragrunt --help
```


## hcl
root
- remote_state
- generate "provider"

subfolder
- include
- dependency
- inputs

## commands
```
terragrunt run-all init    #initialize
terragrunt run-all plan    #pre-check
terragrunt run-all plan *> c:/terragrunt.plan.output #had issues
terragrunt run-all apply   #deploy, this incurs cost!
terragrunt run-all destroy #destroy
terragrunt run-all show -json planfile
```

## execute terraform command on specific module
- cd into that module and run command without run-all, or
- use `--terragrunt-working-dir <module-path>` parameter
