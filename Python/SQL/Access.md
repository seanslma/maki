# Access

## pyodbc LIKE wildcard
LIKE wildcard characters between queries run in Access and from an external applications are different: Access uses the asterisk as the wildcard character, "2019-09-03*"; External application (like Python) uses the percent sign as the wildcard character, "2019-09-03%".

## DAO field type
http://allenbrowne.com/ser-49.html

## DAO connect timestamp
df.timestamp should be changed to str
```py
is_timestamp = pd.core.dtypes.common.is_datetime_or_timedelta_dtype(series)
if is_timestamp:
    changes datetime column to str
```

## DAO connect query
```py
import os
import csv
import win32com.client

def open_db(eng, dbpath, lock=False):
    if not os.path.isfile(dbpath):
        log(f'File does not exist.\n    File: {dbpath}', stop=True)
    #create DAO connection to the access database
    eng = win32com.client.Dispatch("DAO.DBEngine.120")
    mdb = eng.OpenDatabase(dbpath, lock) #True = Lock the database.  Prevent getting to multi-user mode
    return mdb

def get_db_fields(table, csvheader):
    fields = []
    for field in csvheader:
        try:
            fields.append(table.Fields.Item(field))
        except:
            log(f'ERROR: Field "{field}" in csv could not be found in table "{table.Name}"', stop=True)
    return fields

def qry_to_list(mdb, qry, header):
    csv = []
    rs = mdb.OpenRecordset(qry)
    fields = get_db_fields(rs, header)
    while not rs.EOF:
        csv.append([field.Value for field in fields])
        rs.MoveNext()
    rs.Close()
    return csv

def list_to_csv(csvheader, csvdata, csvpath):
    with open(csvpath, 'w', newline='') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(csvheader)
        for row in csvdata:
            w.writerow(row)
```
