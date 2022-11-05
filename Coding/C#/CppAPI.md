# Call c/c++ dll from c#/vb.net

## string parameter
```VB.Net
//void foo(const char *par);
<DllImport(MyDLL, CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Unicode)>
Shared Sub foo(<MarshalAsAttribute(UnmanagedType.LPStr)> ByVal par As String)
End Sub
```

## return string
<DllImport(MyDLL, CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Unicode)>
Shared Function foo() As IntPtr
End Function
Dim pRet As IntPtr = foo()
Dim sRet As String = Marshal.PtrToStringAnsi(pRet)
Dim sRet As String = Marshal.PtrToStringAuto(pRet) ‘ Unix

” vector parameter
void foo(const int par[]);
<DllImport(MyDLL, CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Unicode)>
Shared Sub foo(ByVal par() As Integer)
End Sub

” structure parameter
‘typedef struct {
‘ int x;
‘ double y[2];
‘} struc1;

<StructLayout(LayoutKind.Sequential)>
Structure struc1
Public x As Integer
[MarshalAs(UnmanagedType.ByValArray, SizeConst:=2)]
Public y() as Double
End Structure

‘void foo(struc1 *par);
<DllImport(MyDLL, CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Unicode)>
Shared Sub foo(ByRef par As struc1)
End Sub

Dim myStruc as struc1 = new struc1()
myStruc.x = 1
myStruc.y = new Double(1)
myStruc.y(0) = 1.0
myStruc.y(1) = 4.0
foo(myStruc)

” return structure
‘struc1* foo(void);
<DllImport(MyDLL, CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Unicode)>
Shared Function foo() As IntPtr
End Function
Dim pRet = foo()

” callback function
‘void setCallback(int (*func)(void *handle, const char *msg));
<UnmanagedFunctionPointer(CallingConvention.Cdecl)>
Delegate Function MyCallBack(ByVal handle As IntPtr, <MarshalAsAttribute(UnmanagedType.LPStr)> ByVal msg As StringBuilder) As Integer
<DllImport(MyDLL, CallingConvention:=CallingConvention.Cdecl, CharSet:=CharSet.Unicode)>
Shared Sub setCallBack(ByVal callbackfunc As MyCallBack)
End Sub
Private Function MyCallBackFunc(ByVal handle As IntPtr, ByVal msg As StringBuilder) As Integer
Console.WriteLine(msg.ToString.Trim)
Return 1
End Function
logFunc = New MyCallBack(AddressOf MyCallackFunc)
setCallBack(logFunc)

Please also check for other examples at:
https://docs.microsoft.com/en-us/dotnet/framework/interop/marshaling-classes-structures-and-unions
