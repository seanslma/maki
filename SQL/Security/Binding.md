# Binding

## why bind variables
- avoid injection
- avoid shared pool being flooded by "Literal" SQL statements

The most common cause of ORA-04031 is an application that doesn't use bind variables.
- Bad: `SELECT * FROM users WHERE id = 123;`
- Good: `SELECT * FROM users WHERE id = :user_id;`
  If every query is unique, the Shared Pool gets flooded with thousands of one-time-use execution plans, causing massive fragmentation.
