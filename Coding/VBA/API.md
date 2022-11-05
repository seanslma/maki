# webapi

```vb
Public Function GetApiRes(urlBase as string, uri as string) As Object
    Dim req As Object: Set req = CreateObject("WinHttp.WinHttpRequest.5.1")    
    req.SetTimeouts 0, 30000, 30000, 300000 'ResolveTimeout, ConnectTimeout, SendTimeout, and ReceiveTimeout in milliseconds
    
    req.Open "GET", urlBase & uri
    req.Send
    
    If req.Status <> 200 Then Err.Raise Number:=Err_API_FAILED, Description:="WebAPI call failed: http code " & req.Status
        
    Set GetApiRes = JsonConverter.ParseJson(req.ResponseText)
End Function
```