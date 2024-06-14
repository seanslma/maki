# App Registration

Azure App registrations in Azure Active Directory (AAD) is a service that allows you to register your applications with AAD. 
Once your application is registered, you can use it to authenticate users and access resources on their behalf.

## example
When users login to a website and that website will use the user's login username and password to automatically login to the app.

The generated app registration credentials (`application ID` and `client secret`) will be used to authenticate your application with Azure Active Directory (AAD) and access resources on behalf of users.

To use this for exemple in jupyterhub login, we have to create an `azuread_application`, `azuread_application_password` and `azuread_service_principal`. 
Then in jupyterhub we use the client_id and client_secret to redirect for authentication.

## Types of Azure App registrations:
- **Web applications:** Web applications are applications that are hosted on a web server and can be accessed by users through a web browser.
  When a user visits a web application that is registered with AAD, the web application uses the application ID and client secret to authenticate with AAD and obtain an access token. The web application then uses the access token to access resources on behalf of the user.
- **Native client applications:** Native client applications are applications that are installed on a user's device, such as a computer or mobile phone.
  When a user logs in to a native client application that is registered with AAD, the application uses the application ID and client secret to authenticate with AAD and obtain an access token. The application then uses the access token to access resources on behalf of the user.

## Register your application
When you register your application with AAD, you need to specify the following information:
- A name for your application.
- The type of application your application is (web or native client).
- The redirect URI for your application. The redirect URI is the URL that users will be redirected to after they authenticate with your application.
- The permissions that your application needs to access resources on behalf of users.

Once you have registered your application, you will be given an application ID and a client secret. 
You can use these credentials to authenticate your application with AAD and access resources on behalf of users.

## Where to use it
Azure App registrations are used in a variety of scenarios, such as:
- Authenticating users to web applications and native client applications.
- Accessing resources on behalf of users, such as Microsoft Graph or Azure resources.
- Implementing single sign-on (SSO) for your applications.

Here are some of the benefits of using Azure App registrations:
- **Security:** Azure App registrations provides a secure way to authenticate users and access resources on their behalf.
- **Convenience:** Azure App registrations is easy to use and integrates with other Azure services.
- **Scalability:** Azure App registrations can scale to support a large number of users and applications.

If you are developing an application that needs to authenticate users or access resources on their behalf, then you should consider registering your application with Azure App registrations.

## secret update
https://stackoverflow.com/questions/69045286/invalid-client-secret-is-provided-when-using-correct-and-not-expired-secret

If the app registrations secret is created via terraform, a renewed secret from the portal will not work.
```
AADSTS7000215: Invalid client secret provided. Ensure the secret being sent in the request is the client secret value, not the client secret ID, for a secret added to app
```
We should update the secret from terraform??? No, got the same error.

## get secret id
```sh
az ad app credential list --id <application_id>
```
