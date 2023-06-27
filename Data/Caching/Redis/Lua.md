# Lua

Redis Lua is a scripting feature in Redis that allows you to execute Lua scripts on the server side. 
It provides a way to perform complex operations and manipulations on Redis data using the Lua programming language.

Lua scripting in Redis offers several advantages, including 
- atomicity,
- reduced network round-trips, and
- the ability to execute multiple commands as a single operation
- Lua scripts is as atomic as single commands or MULTI/EXEC

## how Lua scripting works in Redis
- Writing Lua Scripts: use Lua programming language. Redis also provides a set of Lua functions called "Redis Lua Scripting API"
- Loading Lua Scripts: Lua script must be loaded into Redis before use via SCRIPT LOAD command (return script hash)
- Executing Lua Scripts: EVAL command or EVALSHA with the previously obtained script hash
- Script Result: Lua script can return a result, which can be a data structure or a simple value

## returned value
returned values from Lua will be altered (Lua -> Python)
- true/fale: 1/None
- nil: stop returning anything
- float/large float: integer part/min integer (better to return string)
- integer/string: unchanged

## kill script run
- readonly: SCRIPT KILL if executing for longer than `configured lua-time-limit`
- has write: SHUTDOWN NOSAVE to kill Redis (not good) - should always test Lua before prod
