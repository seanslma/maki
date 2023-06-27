# Lua

Redis Lua is a scripting feature in Redis that allows you to execute Lua scripts on the server side. 
It provides a way to perform complex operations and manipulations on Redis data using the Lua programming language.

Lua scripting in Redis offers several advantages, including 
- atomicity,
- reduced network round-trips, and
- the ability to execute multiple commands as a single operation. 

## how Lua scripting works in Redis:
- Writing Lua Scripts:

You can write Lua scripts using the Lua programming language.
Redis provides a set of Lua functions called "Redis Lua Scripting API" that you can use within your scripts to interact with Redis data.
- Loading Lua Scripts: Lua script must be loaded into Redis before use via SCRIPT LOAD command (return script hash)
- Executing Lua Scripts: EVAL command or EVALSHA with the previously obtained script hash
- Script Result: Lua script can return a result, which can be a data structure or a simple value
