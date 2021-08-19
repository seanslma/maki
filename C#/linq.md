# LINQ

## IEnumerable<T> vs IQueryable<T>
Both will be deferred execution. However, there are signoficant differences.

**IEnumerable**<T> is for LINQ-to-object, so all objects matching the original query will have to be loaded into memory from the database. Then the following refined queries will be based on the data in the memory.  For repeated filtering on the original resuluts, it is better to use IEnumerable to avoid several roundtrips to the database.
    
**IQueryable**<T> is the interface that allows LINQ-to-SQL to work. If you further refine your query on an IQueryable<T>, that merged query will be executed in the database, if possible. IQueryable will use expression tree so the code might execute much faster but underlying data provider might not support it.   

## example
```c#
class Customer
{
    public int Id;
    public string Name;
    public string Region;
    public float[] Value;
}

//get iterations into different lists
var lst = new List<Customer>();
var qry = lst.GroupBy(r => new {
    r.Name,
    r.Region,
}).Select(grp => new {
    Key = grp.Key,
    IDs = grp.Select(x => x.Id).ToList(),
}).ToList();

var recordLst = new List<ClientRecord>();
for (int idx = 0; idx < qry.Count; ++idx) {
    var res = qry[idx];
    var key = res.Key;
    List<int> ids = res.IDs;
    var firstCustomer = lst[ids[0]];
    var record = new ClientRecord() { Id = idx, Name = key.Namea, Region = key.Region, Ids = ids, FirstCustomer = firstCustomer };
    recordLst.Add(record);
}
```
