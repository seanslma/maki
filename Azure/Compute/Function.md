# Function

## runtime
- Functions are hosted within Azure App Service
- App Service loads the Azure runtime
- On arrival of a request or the occurrence of a trigger, App Service 
  - loads the incoming payload
  - reads the function.json file to find the function's bindings and trigger
  - maps the incoming data to incoming parameters, and 
  - invokes the function with parameter values
- Once the function completes its execution, the value is passed back to the runtime by way of an outgoing parameter defined as a binding in the function.json file
- The function runtime returns the values to the caller 

## binding
Binding is the process of creating a connection between
- the incoming data and 
- the Azure function along with 
- mapping the data types

Connection type
- a single direction from runtime to function and vice versa or 
- multi directional: transmit data between runtime and function in both directions
- 
## trigger
Trigger can 
- invoke a function based on external events
- pass the incoming data, payload, and metadata to the function
