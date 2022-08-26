# MySQL

```R
require(RMySQL)
 
con = dbConnect(MySQL(), host=svr, port=3307, 
                user=usr, pass=pwd, dbname=dbname)
 
tbs = dbListTables(con)
path = "C:/dat/"
 
for (i in 1 : length(tbs)) {
  tbl = tbs[i]
  fls = dbListFields(con, tbl)
  hasDt = ("LASTUPDATE" %in% fls)
  dtName = ifelse(hasDt, "LASTUPDATE", "SettleTime")
 
  qryTxt = paste("SELECT * FROM", tbl,
                 "WHERE", dtName, ">= '2013-01-01'", 
                 "ORDER BY", dtName, "ASC")
  qry = dbSendQuery(con, qryTxt)
  dat = fetch(qry, n=-1)
  fnm = paste0(path, tbl, ".csv")
  write.table(dat, file=fnm, sep=',', row.names=FALSE, quote=FALSE, na='')
}
 
dbDisconnect(con)
print('all done!')
```
