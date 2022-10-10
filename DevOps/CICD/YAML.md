# YAML

## pass variable by json
https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#converttojson
```
MY_JSON: ${{ convertToJson(parameters.listOfValues) }}
```
https://stackoverflow.com/questions/63502743/pass-variables-to-yaml-template-like-parameters-in-azure-pipelines
```
$obj = ConvertFrom-Json '$(${{ parameters.listOfValuestInJson }})'
```
