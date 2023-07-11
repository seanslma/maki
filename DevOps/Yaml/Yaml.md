<!-- {% raw %} -->
# Yaml

## pass var to yaml
https://stackoverflow.com/questions/48296082/how-to-set-dynamic-values-with-kubernetes-yaml-file
```
template=`cat "deploy.yml.template" | sed "s/{{ MYVARNAME }}/$MYVARVALUE/g"`

# apply the yml with the substituted value
echo "$template" | kubectl apply -f -
```

## pass variable by json
https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#converttojson
```
MY_JSON: ${{ convertToJson(parameters.listOfValues) }}
```
https://stackoverflow.com/questions/63502743/pass-variables-to-yaml-template-like-parameters-in-azure-pipelines
```
$obj = ConvertFrom-Json '$(${{ parameters.listOfValuestInJson }})'
```

<!-- {% endraw %} -->
