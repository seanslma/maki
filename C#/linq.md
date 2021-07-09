# LINQ

```c#
class Customer
{
    public int Id;
    public string Name;
    public string Area;
    public string Region;
    public float[] Value;
}

//get iterations into different lists
var lst = new List<Customer>();
var qry = regPriceLst.GroupBy(r => new {
    r.Name,
    r.Area,
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
    var record = new ClientRecord() { Id = idx, Name = key.Name, Area = key.Area, Region = key.Region, Ids = ids, FirstCustomer = firstCustomer };
    recordLst.Add(record);
}
```
