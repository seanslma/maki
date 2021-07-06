# odbc

```cpp
SQLINTEGER NativeError;
SQLRETURN SQLSTATEs;
SQLSMALLINT i, MsgLen;
SQLCHAR Sqlstate[5], Msg[200];
i = 1;
while ((SQLSTATEs = SQLGetDiagRec(SQL_HANDLE_STMT, stmt.handle(), i,
	Sqlstate, &NativeError, Msg, sizeof(Msg), &MsgLen)) != SQL_NO_DATA) {
    i++;
    std::cout << "the HandleType is:" << SQL_HANDLE_STMT << std::endl;
    std::cout << "the InputHandle is :" << stmt.handle() << std::endl;
    std::cout << "the output state is:" << (char *)Sqlstate << std::endl;	
}
```
