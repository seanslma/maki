# Functions

## install python package
```sh
pip install azure-functions
```

## Install the Azure Functions Core Tools
to allow local debugging
- install from terminal using `npm install -g azure-functions-core-tools`?

## example
https://medium.com/@saurabh.dasgupta1/developing-and-deploying-a-python-azure-function-step-by-step-83c5066a2531

https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local
- create local project: This will create a folder called `MyProjFolder`
  ```sh
  func init MyProjFolder --worker-runtime python --model V2
  ```
- create a `timer trigger` function
  ```sh
  func new --template "Timer Trigger" --name my_timer_trigger
  ```

## issues
"Create in Azure portal" has been disabled for consumption type.
