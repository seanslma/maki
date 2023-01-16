# Jira

## advanced search
```
project = "TEST" AND assignee = currentuser()

status=resolved AND (project="Teams in Space" OR assignee=captainjoe)

#contain words Jira and Software, in no particular order
text ~ "Jira Software"

#exact
text ~ "\"Jira Software\""
```
