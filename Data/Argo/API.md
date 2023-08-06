# API

Argo Server provides the API to programmatically auto tasks.
- url: http://localhost:2746/api/v1
- info: http://localhost:2746/api/v1/info

## access token
To allow the api to automate the tasks, an `access token`, which is a Kubernetes service account token, should be created:
- a `service account` for the automation user:
  ```sh
  kubectl create serviceaccount jenkins
  ```
- a `role` with the right permission:
  ```sh
  kubectl create role jenkins --verb=create,get,list \
  --resource=workflows.argoproj.io --resource=workfloweventbindings --resource=workflowtemplates
  ```
- a `role binding` to bind the role to the service account
  ```sh
  kubectl create rolebinding jenkins --role=jenkins --serviceaccount=argo:jenkins
  ```
- a `service account token` for the service account
  ```sh
  ARGO_TOKEN="Bearer $(kubectl create token jenkins)"
  curl http://localhost:2746/api/v1/info -H "Authorization: $ARGO_TOKEN"
  ```

  ## use api
  API endpoints use json as plyload
  ```sh
  curl http://localhost:2746/api/v1/workflows/argo \
  -H "Authorization: $ARGO_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "workflow": {
      "metadata": {
        "generateName": "my-hello-wf"
      },
      "spec": {
        "templates": [
          {
            "name": "main",
            "container": {
              "image": "docker/whalesay",
              "command": [
                "cowsay"
              ],
              "args": [
                "hello"
              ]
            }
          }
        ],
        "entrypoint": "main"
      }
    }
  }'
  ```

## webhook
The endpoint that is specifically designed to create workflows via an api is `api/v1/events`.
- only allowed to create workflows from a `WorkflowTemplate`, thus is more secure
- only allowed to parse the HTTP payload and use it as parameters
- only allowed to integrate with other systems without having to change those systems
- also supports GitHub and GitLab, so can trigger workflow from git actions

To use the webhook, a `WorkflowTemplate` and a `WorkflowEventBinding` should be created
```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowEventBinding
metadata:
  name: hello
spec:
  event:
    selector: payload.message != ""
  submit:
    workflowTemplateRef:
      name: hello
    arguments:
      parameters:
        - name: message
          valueFrom:
            event: payload.message
```
